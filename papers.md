---
layout: page
---

# Paper Reviews

You are expected to write and submit a paper review of the readings before each class, and answer some questions about the readings.  The review should be akin to a conference paper review.  The purpose of the readings is to provide an illustrative example of the research area.  You are encouraged but not required to read the supplemental readings to better understand the materials.  

You can discuss questions and ask for clarifications with your colleagues and/or on piazza.  You are expected to formulate your own opinion of the reading(s) and write the review yourself.  See for a description of what we expect in paper reviews.  

We may select a random review to read and discuss in class.  This serves to highlight important characteristics of reading papers and writing good reviews.


### Submission

Overview

* Reviews are due **10AM EST one day before lecture** (except for the Indexes paper which is due on Tue, 9/15).  
* Late submissions are given a score of 0 without prior approval.  
* You may miss submissions for up to **4 lectures**.
* To submit:
  * [**Go to the class wiki**](https://github.com/w6113/w6113.github.io/wiki) and click on the appropriate topic
  * Read the instructions at the top
  * Click "Edit" in the upper right. 
  * Add your review

### Reading Tips

Ask the following questions while readings

* What is the context of this work?
  * What was the unmet need or opportunity?  Does it make sense?
  * What were existing approaches and why do they work or not work?
  * What is the simplest example that highlights the problem that this approach works best for?
  * Does the paper (and its contributions) matter?
  * What are the actual hypotheses?
* Approach
  * How do they seek to validate their hypotheses? Do they make sense?
  * Is the evaluation cursory or deep?
  * Do you believe their results?
  * Are the results presented well?


Papers on how to read papers

* [How to Read a Paper - S. Keshav](https://dl.acm.org/doi/pdf/10.1145/1273445.1273458)
* [How to Read a Research Compendium - Nüst et al.](https://arxiv.org/pdf/1806.09525.pdf)

Some papers on reviewing papers

* [Review AntiPatterns (written for FSE 14 PC)](https://homes.cs.washington.edu/~mernst/advice/review-antipatterns-devanbu.txt)
* [Ethics of Peer Review](https://ori.hhs.gov/sites/default/files/prethics.pdf)
* [How NOT to review a paper](https://sigmodrecord.org/publications/sigmodRecord/0812/p100.open.cormode.pdf)
* [Conference Reviewing Considered Harmful](https://homes.cs.washington.edu/~tom/support/confreview.pdf): A view on how reviewing works in practice.



# The Papers

<a name='review1' />
### Review

* Optional: [Architecture of RDBMS Survey](./files/papers/archdbsys-fntdb07.pdf)
* Optional: [What goes around comes around](./files/papers/whatgoesaround-stonebraker.pdf)


<a name='indexes' />
### Indexes    

Readings

* Required: [R-Trees: A Dynamic Index Structure for Spatial Searching](./files/papers/rtree-gut84.pdf)
* Optional: [Generalized Search Trees for Database Systems](./files/papers/gist-vldb95.pdf)
* Optional: [Survey: Modern B-Tree Techniques](./files/papers/btreesurvey-graefe.pdf)
* Optional: [Qd-tree](https://dl.acm.org/doi/10.1145/3318464.3389770)
* Optional: [Tsunami: Learned Multi-dim Indexes](https://arxiv.org/pdf/2006.13282.pdf?TB_iframe=true&width=370.8&height=658.8)

Some things to think about:

* These papers extend indexes to consider multi-dimensional datasets.  Do they address the needs for modern data types (e.g., videos, images, books) and all the things we want to use this data for??  


<a name='join' />
### Joins   

Readings

* Required: [Shapiro: Join Processing in Database Systems with Large Main Memories](./files/papers/gracejoin-shapiro.pdf)
* Optional: [Ripple Joins for Online Aggregation](http://www.cs.cmu.edu/~natassa/courses/15-823/F02/papers/decision-ripple-sigmod99.pdf)



<a name='distjoin' />
### Distributed Joins    

Readings

* Required: [The Gamma database machine project](https://wiki.epfl.ch/edicpublic/documents/Candidacy%20exam/gamma.pdf)
* Optional: [TrackJoin](./files/papers/trackjoin-sigmod14.pdf)
* Optional: [Parallel Database systems: the future of high performance database systems](./files/papers/paralleldbsystems-dewitt.pdf)
* Optional: [Pushing Data-Induced Predicates Through Joins in Big-Data Clusters](http://www.vldb.org/pvldb/vol13/p252-orr.pdf)


<a name='exchange' />
### Exchange Operator    

Readings

* Required: [Encapsulation of parallelism in the volcano query processing system](./files/papers/volcanoparallelism-89.pdf)
* Optional: [SEDA: An Architecture for Well-Conditioned, Scalable Internet Services](http://www.sosp.org/2001/papers/welsh.pdf)


<a name='cascades' />
### Top-down Optimization    

Readings

* Required: [Volcano Optimizer](./files/papers/volcanooptimizer-icde93.pdf)
* Optional: [Orca: A Modular Query Optimizer Architecture for Big Data](./files/papers/orca.pdf)
* Optional: [Cascades](./files/papers/cascades-graefe.pdf)
* Optional: [Cockroach blogpost: How we built a cost-based SQL optimizer](https://www.cockroachlabs.com/blog/building-cost-based-sql-optimizer/)
* Optional: [Book: Inside the SQLServer Query Optimizer](./files/papers/inside-the-sql-server-query-optimizer.pdf)
* Optional: [CH Benchmark](https://db.in.tum.de/research/projects/CHbenCHmark/index.shtml?lang=en)


<a name='colstore' />
### Column Stores    

Readings

* Required: [C-Store: A Column-oriented DBMS ](./files/papers/cstore-vldb05.pdf)
* Optional: [MonetDB/X100: Hyper-Pipelining Query Execution](./files/papers/monetdb-cidr05.pdf)
* Optional: [Integrating Compression and Execution in Column-Oriented Database Systems](./files/papers/abadi-sigmod2006.pdf)
* Optional: [An Experimental Study of Bitmap Compression vs. Inverted List Compression](./files/papers/sidm338-wangA.pdf)
* Optional: [Column-Stores vs. Row-Stores: How Different Are They Really?](http://www.cs.umd.edu/~abadi/papers/abadi-sigmod08.pdf)
* Optional: [Survey: The Design and Implementation of Modern Column-Oriented Database Systems](https://stratos.seas.harvard.edu/files/stratos/files/columnstoresfntdbs.pdf)
* Optional: [Blog Post: 40x faster hash joiner with vectorized execution](https://www.cockroachlabs.com/blog/vectorized-hash-joiner/)


<a name="clouddb" />
### Cloud-scale Analytics

* Required: [Dremel Test-of-Time Keynote](https://www.youtube.com/watch?v=9GutzPX6ufo)
* Optional: [The Snowflake Elastic Data Warehouse](./files/papers/snowflake.pdf)
* Optional: [Dremel: A Decade of Interactive SQL Analysis at Web Scale](http://www.vldb.org/pvldb/vol13/p3461-melnik.pdf)
* Optional: [Original Dremel paper](https://dl.acm.org/doi/pdf/10.14778/1920841.1920886)
* Optional: [Dewitt's Cloud DB talk slides](./files/papers/dewittclouddbtalk.pptx)
* Optional: [Choosing a Cloud DBMS](./files/papers/choosingclouddb.pdf)


<a name='compilation' />
### Query Compilation    

Readings

* Required: [Efficiently Compiling Efficient Query Plans for Modern Hardware](./files/papers/p539-neumann.pdf)
* Optional: [How to Architect a Query Compiler, Revisited](./files/papers/tahboub-sigmod18.pdf)
* Optional: [Generating code for holistic query evaluation](./files/papers/krikellas-icde2010.pdf)
* Optional: [Spark's Scala expression compiler code](https://github.com/apache/spark/blob/master/sql/catalyst/src/main/scala/org/apache/spark/sql/catalyst/expressions/codegen/CodeGenerator.scala)
* Optional: [MemSQL's blogpost](http://highscalability.com/blog/2016/9/7/code-generation-the-inner-sanctum-of-database-performance.html)

Some things to think about when reading

* For disk-based systems, when would query compilation be useful?




<a name='udfs' />
### Hybrid Caching/UDFs    

Readings

* Required: [Hybrid Caching](./files/papers/caching-sigmod1996.pdf)
* Optional: [Tuplex: Data Science in Python at Native Code Speed](http://cs.brown.edu/~lspiegel/files/Tuplex_Preprint2020.pdf)
* Optional: [Exploiting Correlations for Expensive Predicate Evaluation](https://arxiv.org/pdf/1411.3374.pdf)
* Optional: [Optimization of Queries with User-defined Predicates](http://www.vldb.org/conf/1996/P087.PDF)
* Optional: [Probabilistic Predicates](https://www.microsoft.com/en-us/research/publication/accelerating-machine-learning-queries-with-probabilistic-predicates/)
* Optional: [Froid: Optimizing Imperative Programs in RDBMSes](./files/papers/froid.pdf)
  * [Research Talk](https://www.youtube.com/watch?v=Xyvpcf2RtO4)
* Optional: [Compiling PL/SQL Away](https://arxiv.org/pdf/1909.03291.pdf)
* Optional: [Flare: Optimizing Apache Spark with Native Compilation](https://www.usenix.org/system/files/osdi18-essertel.pdf)


<a name='dataflow1' />
### Large-scale Data Flow

Readings

* Required: [MapReduce](https://www.usenix.org/legacy/events/osdi04/tech/full_papers/dean/dean.pdf)
* Required: either [RDDs](https://sfu-db.github.io/dbsystems/Papers/nsdi12-final138.pdf) or [SparkSQL](https://sfu-db.github.io/dbsystems/Papers/SparkSQLSigmod2015.pdf)
* Optional: [Spark (mainly examples)](http://static.usenix.org/events/hotcloud10/tech/full_papers/Zaharia.pdf)
* Optional: [State of the Art in Large scale Data Flow](./files/papers/kossmann-sotadistdbs.pdf)
* Optional: [DyadLinq](http://michaelisard.com/pubs/sigmod09.pdf)



<a name='naiad' />
### Minibatch/incremental Dataflow

Readings

* Required: [Naiad: A Timely Dataflow System](https://www.microsoft.com/en-us/research/wp-content/uploads/2013/11/naiad_sosp2013.pdf)
  * [A video introduction to Timely](https://www.youtube.com/watch?v=yOnPmVf4YWo)
  * Timely is now a company called Materialized.  [Try their software!](https://materialize.io/)
* Optional: [Discretized Streams](https://people.csail.mit.edu/matei/papers/2013/sosp_spark_streaming.pdf)
* Optional: [Earlier CIDR paper](https://www.microsoft.com/en-us/research/wp-content/uploads/2013/01/differentialdataflow.pdf)
* Optional: [Timely Dataflow](https://github.com/TimelyDataflow/timely-dataflow)

Some notes to guide your reading and thinking.  

* This paper focuses primarily on what Naiad provides and how it works.  But which are actually _necessary_?  Which are nice-to-haves?  Why?  How does it contrast with other papers we have read (spark, spark streaming, recursive queries)?  Can it do things other systems cannot?   
* What makes this paper easy or hard to read?  Note those, and other questions you have, in the comments, and we can discuss in class
* We will go over some of the technical details of how execution operates

<a name='matviews' />
### Materialized Views    

* Required: [Survey: Materialized Views](./files/papers/matview-survey.pdf) Ch 1,2,4
* Optional: [Noria: dynamic, partially-stateful data-flow for high-performance web applications](https://pdos.csail.mit.edu/papers/noria:osdi18.pdf)
* Optional: [CrocodileDB: Efficient Database Execution through Intelligent Deferment](http://cidrdb.org/cidr2020/papers/p14-shang-cidr20.pdf)

<a name="incmatviews" />
### Incrementally Maintaining Materialized Views

* Required: [DBToaster](https://dbtoaster.github.io/papers/pvldb2012-dbtoaster.pdf)
  * Optional: [DBToaster talk](https://dbtoaster.github.io/papers/ecocloud2013-dbtoaster-mn.pdf)
  * Optional: [The theory](https://dbtoaster.github.io/papers/pods2010-ring.pdf)
* Optional: [CrocodileDB: Efficient Database Execution through Intelligent Deferment](http://cidrdb.org/cidr2020/papers/p14-shang-cidr20.pdf)


<a name='datalog' />
### Datalog and Recursion   

Readings

* Required: [Datalog and Recursive Query Processing](https://www.nowpublishers.com/article/Details/DBS-017) Chapters 2, 3
* Optional: [Evita Raced: Metacompilation for Declarative Networks](http://www.vldb.org/pvldb/1/1453978.pdf): query optimization AS datalog

Questions

* When you assess the reading, compare against other formal and informal data query languages we have encountered.  



<a name='lineage' />
### Lineage   

Readings:

* Required: [Provenance Semirings](http://users.ics.forth.gr/~gregkar/publications/pods2007.pdf)
* Optional: [SMOKE: Fine-grained Lineage at Interactive Speed](http://www.vldb.org/pvldb/vol11/p719-psallidas.pdf)


Question to comment on:

* Provenance goes beyond what they mention in the paper and is _everywhere_.  Point out a concept/functionality in the real (or digital) world that can be recast as provenance and provenance queries.  Describe it.

<a name='lineage2' />
### Lineage Systems

Read one of the two required papers:

* Required: [SMOKE: Fine-grained Lineage at Interactive Speed](http://www.vldb.org/pvldb/vol11/p719-psallidas.pdf)
* Required: [Perm: Processing provenance and data on the same data model through query rewriting](https://www.zora.uzh.ch/id/eprint/24446/2/main.pdf)
* Optional: [GPROM: Middleware implementation for PERM](https://par.nsf.gov/servlets/purl/10082097)
* Optional: [Provenance for Interactive Visualizations](https://www.dropbox.com/s/32aid7isd2arx47/smoke-hilda18-cr.pdf?dl=0)
* Optional: [Titian: Data Provenance Support in Spark](http://www.vldb.org/pvldb/vol9/p216-interlandi.pdf)


<a name="replication" />
### Distributed Consistency under Replication

* [The original Raft paper](https://raft.github.io/raft.pdf)
* (Optional) [Viewstamped Replication Revisited](http://pmg.csail.mit.edu/papers/vr-revisited.pdf)
* (Optional) [Living Without Atomic Clocks blog post](https://www.cockroachlabs.com/blog/living-without-atomic-clocks/)
* (Optional) [Raft Refloated](http://www.cl.cam.ac.uk/~ms705/pub/papers/2015-osr-raft.pdf) 
* (Optional) [Google's Paxos Made LIve](https://research.google.com/archive/paxos_made_live.html)
* (Optional) [Anna: A Crazy Fast, Super-Scalable, Flexibly Consistent KVS](https://rise.cs.berkeley.edu/blog/anna-kvs/)




<!--
<a name='mockpc' />
### MockPC  

Readings:

* Your assigned papers
-->



<a name="sysr"/>
### System R Overview 

Readings 

* Required: <a href="./files/papers/systemr-retrospective.pdf">System R Retrospective</a>
* Optional: <a href="./files/papers/ingres-retrospective.pdf">Ingres Design</a>


Paper Review 

* System R was an impressive research and engineering effort, and the reading is a retrospective of the 6 year project.  
* The paper discusses "the Convoy Problem".  Discuss the problem:  What is it?  Why does it exist?
* The paper discusses many many topics.  Identify and pick one aspect (different than the convoy problem) that you are particularly impressed with.  Discuss what and why.


<a name='postgres' />
### INGRES/POSTGRES    

Readings

* Required: [Design of Postgres (Initial design)](./files/papers/postgres-retrospective.pdf)
* Optional: [The Postgres Next-Generation DBMS (Midterm design)](./files/papers/postgres-nextgen-cacm.pdf)
* Optional: [Design of INGRES](./files/papers/ingres-retrospective.pdf)
  * Worth skimming: QUEL, leveraging UNIX, concurrency control arguments
* Optional: [The Landsharks are on the Squawk Box - Stonebraker Turing Award Lecture](https://cacm.acm.org/magazines/2016/2/197423-the-land-sharks-are-on-the-squawk-box/fulltext)


Paper Review 

* What were the main goals for the Postgres system and why do you think they chose those goals?  Do they make sense?
* Pick one of the (many) ideas in the paper that most interests you.  Why is it interesting?   Does the proposed design hold water?  Feel free to read related work.


<a name="optional" />
## Unscheduled Topics


<a name='oltp' />
### OLTP Stores    

Readings

* Required: [OLTP Through the Looking Glass, and What We Found There](./files/papers/oltpperf-sigmod08.pdf)
* Optional: [Hekaton: SQL Server’s Memory-Optimized OLTP Engine](./files/papers/hekaton-sigmod13.pdf)
* Optional: [The End of an Architectural Era](http://nms.csail.mit.edu/~stavros/pubs/hstore.pdf)




<!--
<a name='sampling' /> 
### Visualization/Sampling

* Required: [BlinkDB](https://sameeragarwal.github.io/blinkdb_eurosys13.pdf)
* Optional: [Dynamic Sample Selection for Approximate Query Processing](http://www-cs-students.stanford.edu/~babcock/papers/sampling.pdf)
-->

<a name="serverless"/>
### Serverless Querying

* Required: [Cloudburst: Stateful Functions-as-a-Service](https://arxiv.org/abs/2001.04592)
* Optional: [Autoscaling Tiered Cloud Storage in Anna](https://dsf.berkeley.edu/jmh/papers/anna_vldb_19.pdf)
* Optional: [Starling: A Scalable Query Engine on Cloud Function Services](https://arxiv.org/pdf/1911.11727.pdf)


<a name="mlindb" />
### ML in DB

* Required: [MAD Skills: New Analysis Practices for Big Data](http://db.cs.berkeley.edu/papers/vldb09-madskills.pdf)
* Required: [Dan Olteanu's VLDB 2020 Keynote](https://www.youtube.com/watch?v=0ic0jMjOpM0) and skim [the paper](http://www.vldb.org/pvldb/vol13/p3502-olteanu.pdf)
* Optional: [Towards a Unified Architecture for in-RDBMS Analytics](https://cs.stanford.edu/people/chrismre/papers/bismarck.pdf)
* Optional: [Learning Generalized Linear Models Over Normalized Data](http://pages.cs.wisc.edu/~jignesh/publ/GLMs-over-joins.pdf)



<a name='selftuning' /> 
### Self-tuning DBs  

* Required: [Self-Tuning Database Systems: A Decade of Progress ](./files/papers/selftuning-chaudhuri-vldb07.pdf)
* Optional: [Automatically Indexing Millions of Databases in Microsoft Azure SQL Database](https://www.microsoft.com/en-us/research/uploads/prod/2019/02/autoindexing_azuredb.pdf)
* Optional: [Query-based Workload Forecasting for Self-Driving Database Management Systems](https://www.cs.cmu.edu/~dvanaken/papers/forecasting-sigmod18.pdf)
* Optional: [Database Cracking](https://stratos.seas.harvard.edu/files/IKM_CIDR07.pdf)

<a name="learned" />
### Learned and Adaptive Indexes

* [From Auto-tuning One Size Fits All to Self-designed and Learned Data-intensive Systems](https://stratos.seas.harvard.edu/files/stratos/files/selfdesignedandlearnedsystems.pdf)


<a name='joinopt' />
### Join Optimization

* Required: [Dynamic programming strikes back](https://dl.acm.org/doi/pdf/10.1145/1376616.1376672)
* Required: [Worst Case Optimal Joins](https://columbiadb.github.io/files/papers/optimaljoin.pdf)
* Optional: [Learning to Optimize Join Queries With Deep Reinforcement Learning](https://arxiv.org/pdf/1808.03196.pdf)
* Optional: [SkinnerDB: Regret-Bounded Query Evaluation via Reinforcement Learning](https://arxiv.org/pdf/1901.05152.pdf)
* Optional: [Selectivity Estimation using Probabilistic Models](https://ai.stanford.edu/~koller/Papers/Getoor+al:SIGMOD01.pdf)


<a name='aqp' />
### Approximate Query Processing

* Required: [BlinkDB](https://sameeragarwal.github.io/blinkdb_eurosys13.pdf)
* Optional: [Pfunk-H](https://columbiaviz.github.io/files/papers/pfunk.pdf)
* Optional: [Sample+Seek](https://columbiaviz.github.io/files/papers/sigmod16sampleseek.pdf)
* Optional: [WanderJoin](https://columbiaviz.github.io/files/papers/wanderjoin.pdf)
* Optional: [Rapid Approximate Aggregation with Distribution-Sensitive Interval Guarantees](https://arxiv.org/pdf/2008.03891.pdf)

<a name='stream' />
### Windows and Streaming

* Required: [The Dataflow Model](http://www.vldb.org/pvldb/vol8/p1792-Akidau.pdf)
* Optional: [Continuous Query Language](http://ilpubs.stanford.edu:8090/758/1/2003-67.pdf) 


<a name='scans' />
### Fast Scans

* Required: [Column Sketches](https://stratos.seas.harvard.edu/files/stratos/files/sketches.pdf)
* Required: [BitWeaving](http://www.cs.wisc.edu/~jignesh/publ/BitWeaving.pdf)
* Optional: [WideTables](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.650.2556&rep=rep1&type=pdf)
* Optional: [Vectorizing Database Column Scans with Complex Predicates](http://www.adms-conf.org/2013/muller_adms13.pdf)


<a name='lineage3' />
### Using Lineage

* Optional: [Querying and Creating Visualizations by Analogy](http://www.cs.utah.edu/~juliana/pub/tvcg-analogy2007.pdf)
* Optional: [VisTrails: Enabling Interactive Multiple-View Visualizations](https://vgc.poly.edu/~juliana/pub/vistrails-vis2005.pdf)

<a name='datacubes' />
### Data Cubes    

* Required: [Data Cube](./files/papers/datacube-jimgray.pdf)
* Optional: [Implementing Data Cubes Efficiently](http://ilpubs.stanford.edu:8090/102/1/1995-34.pdf)
* Optional: [Explaining differences in multidimensional aggregates](./files/papers/olapdiff-sunita.pdf)
* Optional: [Gaussian Cubes: Real-Time Modeling for Visual Exploration of Large Multidimensional Datasets](https://cscheid.net/static/papers/infovis_gaussian_cubes_2016.pdf)

<a name="obliv"/>
### Oblivious Databases

* Required: [ObliDB](http://www.vldb.org/pvldb/vol13/p169-eskandarian.pdf)
* Optional: [Efficient Oblivious Database Joins](http://www.vldb.org/pvldb/vol13/p2132-krastnikov.pdf)

<a name='eddies' />
### Eddies  

Readings

* Required: [Eddies: Continuously Adaptive Query Processing](./files/papers/eddies-sigmod00.pdf)
* Optional: [Survey: Adaptive Query Processing](https://www.nowpublishers.com/article/Details/DBS-001)
* Optional: [TelegraphCQ: Continuous Dataflow Processing for an Uncertain World](http://db.csail.mit.edu/madden/html/TCQcidr03.pdf)

Address the following in your review's details:

* This question asks you to separate the ideas in eddies from its implementation.  Imagine eddies became the canonical engine design, and its _core ideas_ continued to be improved.
  * Come up with the most interesting query/workload for which such an engine would really shine.  What are its properties?
  * Come up with the most interesting query/workload that would cripple such an engine.  What are its properties?  



<a name="pvd"/>
### Physical Database Design

* TBA
