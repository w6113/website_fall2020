---
layout: page
---

# Reviews

In reviews, good to compare how you would have designed the component/system given
the use cases/constraints, before reading the paper's solutions, with how it was actually implemented

* Good writing
* Riva points to timescale's (blog post about columnar compression)[https://blog.timescale.com/blog/time-series-compression-algorithms-explained/]
* what if insertion or update ops change a small part of data, but distribution changes because of it
  sholud c-store change compression strategy?
  -> could do it in the background by creating a new projection.  Replicas
* WS and RS have 1-1 mapping of segments/order
  * how to find a partitioning scheme when dataset is large
  -> walk through how updates/deletes work
* How should Segments be defined?  pros and cons


# Column Stores (OLAP)

Background

* OLAP is fundamentally about throughput
  * disk scans, memory throughput, CPU throughput (instructions/tuple)
  * We care about _effective throughput_ meaning useful bytes / sec
    * reading a page that will be filtered out means 0 useful bytes 
* Hardware trends since 70s
  * CPUs >10000x faster
  * Disk bandwidth / Disk capacity reduced by 100x
  * Seq / random acces increased by 10x
  * Memory latency vs CPU cycle increased 100x
* Two major systems
  * C-store addresses memory and disk bottlenecks
    * Better utilize work per byte of bandwidth from disk
    * storage format, compression, query execution, shared nothing
  * MonetDB/X100 addresses CPU and memory bottlenecks
    * Better utilize each byte sent to CPU 
    * vectorized operators, compiler optimizations (simd, loop pipelining, avoid branch mispredictions)
    

The bag of tricks

* virtual IDs
  * just store array of values.  array index _is_ the row id
* block/vectorized processing
  * fixed amount of data processed at a given time.  Usually multiple of page size
* late materialization (keep columns rather than multi-col tuples)
* Column compression + compressed execution
* Specialized joins over compressed columns
* Replicate cols on different sort orders
* Adaptive column sorting (cracking)
* Bulk loading

Row vs Col page structure

* Row pages (NSM Nary storage model) data top down, and pointers to rows bottom up

        [[header] [row 1], [row 2], ...

                [row 2 ptr] [row 1 ptr]]

* Col pages (DSM decomposition storage model)
  * Each page contains one column's data
  * Classic DSM explicitly stores rid.  Scan is slower than NSM when >30% of cols are projected
  * Improved in C-store to 70%.  80% on flash due to no disk head seeks

        [[header] [rid1], [val1], ... ] Subrelation for Col 1

* PAX: hybrid.  Each page contains K rows, internally columnar (for CPU)
* Fractured mirrors: each replica stored in row/col format


### C-Store

Motivation

* Logging

        10k machines * 100hz = 1,000,000 
        * # Sensors * # data centers 
  * bulk writes, few updates, read-mostly

* Star schema
  * unnormalized retailer schema 

        store_id, store_name, store_owner, store_addr1, ....,
        emp_id, emp_name, emp_age, emp_salary, ...
        prod_id, prod_name, prod_id, prod_price, ...
        ...

  * Redundancy, big issuse, it's bad
    * update/delete anomalies
  * normalized "star" schema
    
        fact(store_id, emp_id, prod_id, cust_id, ...)
        store(store_id, name, owner, addr1, ...)
        ...

  * Why do this?
    * read less data since only care about a few attributes
    * avoid anomalies

Overview

* supports the logical relational model
* So much data that indexes don't help and in fact _hurt_ in most cases 
  * good if reading a few records/pages (we'll get to that for OLTP)
* performance bottlenecked by read throughput 
* want 100x speed up compared to existing solutions
  * data cubes 
    * expensive -- OLAP queries access different sets of attributes
    * restrictive -- for constrained queries (algebraic, distributive)
    * but can still be built (faster) on column stores
* Notice:
  * Hybrid WS vs RS: write buffer vs read optimized storage
    * Now seen as HTAP systems
  * Most wins come from compressed execution, yet big chunk of paper discusses correctness.  Why?
  * There's a story for multi-node, but kind of an aside here


#### Physical layout

Projection: Multiple columns from a table

* Must be set of covering projects for each table
* each column in project is stored separately
* sorted on subset of the columns (sort key).  Index in sort order is storage key for row.

      EMP1(name, age | age)  # sorted on age

* The columns for EMP1:

      (name, storage_key)
      (age, storage_key)

      // storage key not stored, just its order number in the column
      // for joining between projections
* Each projection horizontally partitioned by value on sort key into segments
  * segment = key range.  Can use segment header to store other metadata
  * thus name, age are identically partitioned


Join Indexes match the same records across projections

* Maps rows from segment k in projection C1 to corresponding storage keys in C2
* Suppose I have the following query and projections

        SELECT a, b FROM data

        C1(a | a)  # M partitions
        C2(b | b)  # N partitions

        C1_i is i'th partition of C1
        J_i(sid, storage_key)  

        * has same number of rows as C1_i.
        * sid, storage_key of matching row in C2

* Expensive to maintain under updates!  
  Try to avoid by having each col in many projections so join index isn't needed

Invisible Join for star schemas

                                   store(sid, loc)
                                 /
        fact(id, sid, eid, pid)  = emp(eid, age)
                                 \
                                   product(pid, name)

        
        res(id) :- fact(id, ...) store(sid, 1)
                                 emp(eid, 18)
                                 product(pid, 'amy')

* Normally, pipelined joins. Problem is output of join is two lists of
  ids, one from each table, but only one will be in sorted order.
  Next joins will be expensive
* Invisible join turns join into filters on dimensions and bitmap intersections
  * filter store, emp, product, 
    keep hash table where key is the sid/eid/pid of matching rows
  * scan fact table's sid/eid/pid cols, probe has table. Produce bit vector
  * Intersect bit vectors to complete the join

Misc

* Example query + projection
* overlapping projects
* Picking projections is an optimization problem limited by storage space
  * if don't have a projection for query, gets expensive





Compression

* few distinct values, sorted on this col

      (val, startidx, endidx)

* Runlength encoding

      10, 10, 10, 10, 11 --> (10,4), (11,1)
      
      combine with delta compression

      0, 0, 0, 0, 1 --> (0, 4), (1, 1)  # 2 bits each

* bitmaps

      (val, bitmap) e.g., (99, 0111100010100)

* delta compression

      10, 12, 13, 14 --> 10,2,1,1
      reduce bits per val, then compress again

* What data types/use cases are these good for?
  * Numbers
  * Strings usually dictionary encoded.  Apply predicates to
    dictionary, retrieve the string ids that pass
* So fast that CPU decompression is often bottleneck!
* Recent work from VLDB 20:
  * Model string columns as columnar tables by detecting regex-like patterns
  * Treat each column as a "mini" column and dense pack

What is downside of compression?

* CPU to decompress
* More book keeping
* N operators * M compression methods worth of code...
* Morphstore VLDB 20
  * Automatically wrap existing operators for uncompressed or specific combos of compression
    with on the fly de/re-compression or re-morphing

      U \
          OP - U   if inputs are compressed via D, E
      U /           and next op expects F, then autogenerate:

      D->U \
             OP - U->F
      E->U /

      



#### Write Store (WS)

How would you have designed the write store if you hadn't read the paper?

* Why the same physical layout as the read store?
* Why snapshot isolation?
* Why high _and_ low watermarks?
* Why store storage key explicitly?

Tries to avoid building two engines.

* also column store
* same physical design as RS (projections, join indexes, horizontal partitioning) 
* columns store the storage key explicitly
* storage key > key in largest RS segment.  
  * **Thus (sid, storage key) is globally unique**
  * join indexes naturally index into WS
* uncompressed, b-tree indexed, likely in mem
  * two indexes: one on sk, the other on sort key

        EMP(age,name|age)

        btree index on sk --> age
        btree index on sk --> name
        btree index on age --> smallest sk of the run


Implementation

* BerkeleyDB + lots of memory

Why is serializability/locking undesirable?

* Workload: large reads, fewer OLTP queries, continuous/bulk inserts


Snapshot Isolation

* Inserts may be continuous.  Reads must be run in snapshot isolation
  * No updates in place, everything is timestamped
  * Coarse epochs for timestamps
* Low and high watermarks
  * High: latest time big reads can run in snapshot isolation
  * Low: earliest time big reads ta run (why? to avoid keeping arbitrary timetravel state)
* Run in epochs.    Central epoch provider (timestamp authority TA)
  * Each projection segment in WS keeps insert vector (insert epoch for each row) and deleted vector

        EMP(age,name|age) essentially stored as
        EMP(age,name,_insert,_deleted|age)

        age data:
        [18, 20, 30, ...]
        age insert vector:
        [1 1 2 ...]
        deleted vector
        [x x 3 ...]    first two not deleted, third deleted in epoch 3
    
  * TA sends new epoch messages to nodes
  * nodes wait until all active xacts commit locally, then reply OK
  * TA sets new HWM, sends to nodes
  * HWM is safe to read
* Tuple Mover (TM) 
  * Look for pairs of segments from WS, RS
  * Merge all inserts/deletes into a new RS' segment where timestamps < LWM
    * reminds of LSM tree in being scan optimized, where in-memory batches sort-merged into 
      write-optimized disk batches.  Ivented by Pat & Betty o Neil, who also worked on C-store
    * update join indexes :(
  * Thus, can do time travel between LWM - HWM.


#### Why not implement in a rowstore

* vertical partition the row store  
  * tuple overhead and storing pkeys substantial
    * 17 col table is 4GB compressed
    * single attr is 1GB compressed
      * 4 bytes for data, 8 bytes for header, 4 bytes for pkey
  * C-store: 240MB/col
* Mat views do well, but suffer the overheads, and limited to recurring queries (not adhoc)

Isn't storing all these projections blowing up disk costs by several X?

* Compression such a big deal, can afford to
* Disk _space_ usually not a problem, it's disk throughput per _effective_ byte of data
  * See hardward trends at the top
* Each query accesses few projections

#### Query execution walk through

        select avg(price)
        from data
        where symbol = 'GM' AND date = xxx

Row store

* read and send entire tuples throughout the plan
        
                         AVG price
                            |
                     SELECT date = xxx
                            |
                      SELECT sym = 'GM'
                            |
                            |   (GM, 1, ... xx, ...)
                            |
        [Symbol, price, nshares, exchange, date,...]
        [GM        1    ...                 xx     ]
        [GM        2    ...                 xx     ]
        [GM        3    ...                 xx     ]
        [AAPL      4    ...                 xx     ]
        ...



Columnar using row store

* send complete tuples up after `construct()`
* due to record overhead, can be slower than vanilla row store

                           Avg price
                                |
                        SELECT date = xx
                                |
                        SELECT sym = GM
                                |
                                |   (GM, 1, xx)
                                |
                  Construct (Symbol, Price, Date)
               /     |                              \
        [Symbol]   [price]   [nshares]  [exchange]  [date] ...
          GM        1                                 xx  
          GM        2                                 xx
          GM        3                                 xx
          AAPL      4                                 xx


CStore w/ late materialization

* removes record headers
* send bitstrings through query plan

                           Avg price
                                |    (1,2,3)
                          Lookup price
                                |    (1,1,1,0)
                               AND
                 (1,1,1,0)  /        \   (1,1,1,1)
            SELECT sym = GM            SELECT date=xx
               /                                   \
              /                                      \
        [Symbol]   [price]   [nshares]  [exchange]  [date] ...
          GM        1                                 xx  
          GM        2                                 xx
          GM        3                                 xx
          AAPL      4                                 xx

CStore w/ compression     

* send compressed bitstrings


                           Avg price
                                |    (1,+1,+1)
                          Lookup price
                                |    (3x1, 1x0)
                               AND
                 (3x1,1x0) /        \   (4x1)
            SELECT sym = GM            SELECT date=xx
               /                                   \
              /                                      \
        [Symbol]   [price]   [nshares]  [exchange]  [date] ...
         3xGM         1                             4x "xx"
         AAPL        +1                                 
                     +1                                
                     +1                               


* Why the wins?
  * biggest wins from compression:   10x
    * compress better and read less
  * late materialization: bit strings instead of tuples:  ~3x
  * block-based execution: 
    * row-based: ~2 function calls e.g., `tuple.get_attr('id')` per tuple 
    * block: single operator call + loop   ~1.5x
    * has nice low level hardware properties (cache line, prefetch, simd, parallelization)

Bitmaps are really important.  Lots of work on bitmap compression.  

* Experimental Study of Bitmap and Inverted List Compression
  * From class project
  * ton of experiments on 9 bitmap, 12 inverted list compression methods
* example: 1, 2, 5, 10
* Bitmap compression: take bitvector, compress.  Usually variation of run length encoding

      [ 0 1 1 0 0 1 0 0 0 0 1 ]

  * Roaring partitions the number space, uses diff encoding for each partition based on 
    cardinality of each partition
  * Roaring has fastest intersection -> top-k, join, conjunctions
* Inverted list: list of numbers that are set instead of bitvector
  * delta compress by blocks
  * usually less space unless list is very dense
  * decompresses faster
  * faster union --> disjunctions, range queries

      [ 1, 2, 5, 10 ] -delta compress-> [ 1, 1, 3, 5 ]

    


Highlights:

* >100x faster than RDBMS -- everyone uses it
* may not be as fast for random writes.
  * ensure sorted in every projection.
  * is this a problem?

## MonetDB/VectorWise

Two awesome systems.  The x100 CIDR paper is great.

* Marcin who built this and the successor vectorwise went on to found snowflake

MonetDB

* Optimized for CPU
  * CPU pipelines are super long (>30 stages in 2004), expensive to flush on misprediction
  * Data-dependent conditionals are very expensive
  * Maximize instructions per cycle, cpu cache hit rate
* On a single table filter project groupby query (TPCH Q1)
  * mysql only spends 10% of cpu doing the work.  
  * 30% on hash table creation+lookup
  * 60% on interpretor overheads (get ith field)
* overhead of inidivdual instructions
  * "plus" costs 38 instructions
  * C's + costs 4 instructions
* Highlights 
  * "Zero degrees of freedom": no interpretation on the data path
    * Operators don't have predicates
    * Each expression (e.g., +, -) is a physical Binary Association Table (BAT) operator
  * full column stored at a time.  Stores id and value 
  * BAT column-at-a-time physical algebra

        sum(c * (1 - d)), sum(c * (1 - d) * e)

        tmp1 = -(1, d)
        tmp2 = *(c, tmp1)
        tmp3 = sum(tmp2)
        tmp4 = *(tmp2, e)
        tmp5 = sum(tmp4)

  * Physical expression operators (e.g., +, /) that are col-at-time
  * Optimized to minimize PUC cache misses
  * cracking
* Limitations
  * lacks pull-based pipelining
  * materializes all intermediates.  massive write bandwidth
  * columns uncompressed
  * memory mapping -- relies on OS for I/O scheduling

Vectorwise

* Volcano based data flow, but processes vectors of ~L1 cache size
* Heavily templated, vectorized physical operator implementations
  * uses input types + auto-variations (e.g., branch/nobranch) to generate
    ~5000 primitive/physical functions!
  * note: type management is becoming a deal in modern DBs
* Compression and other tricks
* Profiling per-vector is cheaper, can keep good stats
* Adaptively try different physical implementations on a per-vector(s) basis (uses bandits)
  * consider less than implementation

          branching_lt(n, res, col, val):
            k = 0
            for i in 0..n
              if (col[i] < val) res[k++] = i


          nonbranching_lt(n, res, col, val):
            k = 0
            for i in 0..n
              res[k] = i
              k += (col[i] < val)

  * nonbranching is always the same cost, and better than branching EXCEPT in very low selectivity case!
  * use RL.  Reward is regret assuming had used best flavor.  
  * Each flavor is a random process, but nonstationary, so trickier.
  * see: Microadaptivity in Vectorwise
