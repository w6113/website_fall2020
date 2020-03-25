---
layout: index
---


#### Overview

This course is intended as an advanced graduate-level course in database systems research.  
The content will cover classic and modern database systems research.  Topics will range from classic database system design, modern optimizations in single-node and multi-node settings, data cleaning and explanation, and data provenance.

The class places a _heavy emphasis on paper reading and writing good paper reviews_.   The point is to practice reading papers critically, writing proper reviews, implementing ideas in research papers, and conducting research.  As such, students will be expected to read papers in depth, complete assignments based ideas from the readings, and conduct a semester-long research project.

Students are expected to be comfortable with a range of programming languages, reading code, actively participate in discussions, and presenting.

<small style="color: grey">Course capped at 25.  If waitlist is huge, an assignment will be used to choose participants.</small>



#### Recent Announcements

* [Submit Camera Ready on CMT website](https://cmt3.research.microsoft.com/W61132019/) by 5/10 11:59PM EST
* Link to [list of your reviews this semester](./exreviews).
* Project submissions updated
  * Presentations on May 2nd in class.  10 minutes per group
  * Project reports due May 10th 11:59PM EST.
* Added [submission form for PC Meeting reflection](https://forms.gle/wmqKEU1AW4bMs3G4A), due Sat 4/6 11:59PM
* Paper Draft due date has been moved to March 22nd, and PC Reviews to March 29th.
* Due to popular request, paper reviews can be turned in 10PM EST day before class.
* Updated [Projects page](./projects) with project milestones and a few example projects.
* Uploaded [list of students that successfully completed HW0 and can enroll in the course](./md5s)
* [Sign up to lead a lecture/paper discussion](https://piazza.com/class/jpqearvq2qq201?cid=11)
* Added page for [paper reviews](./reviews)

#### Schedule


<style>
.presenter { }
</style>

<table class="table table-striped schedule">
  <thead>
  <tr>
    <!--<th class="idx" style="width: 3em; max-width:3em;"></th>-->
    <th class="date" style="width: 4em; max-width: 4em;"> <p> <span>Date </span> </p> </th>
    <th style="min-width: 15%;"> <p> <span>Topic </span> </p> </th>
    <th style="width: 10%"> <p> <span>Notes </span> </p> </th>
    <th style="width: 10%"> <p> <span>Readings </span> </p> </th>
    <th style="width: 15%;"> <p> <span>Assigned</span> </p> </th>
    <th style="width: 15%;"> <p> <span>Due</span> </p> </th>
  </tr>
  </thead>
{% assign idx = 0 %}

{% for r in site.data.schedule %}
  {% assign idx = idx | plus: 1  %}
  <tr style="background-color: {{r.color}}; ">
    <!--<td class="idx">L{{idx}}</td>-->
    <td class="date">L{{idx}}: {{r.date}}</td>
    <td class="slug">
      <b>{{r.slug}}</b>
      {% if r.presenter %}
        <br/>
        <span class='presenter'>Presenter: {{r.presenter}}</span>
      {% endif %}

      </td>
    <td class="notes">
      {% if r.link %}
        <a href="{{r.link}}">Notes</a>
      {% endif %}
    </td>
    <td class="readings">
      <a href="./reviews#lec{{idx}}">Readings</a>
    </td>
    <td>{{r.assigned | safe}}</td>
    <td>{{r.due | safe}}</td>
  </tr>
{% endfor %}
</table>



#### Tentative list of papers for last lectures

* Approx Query Processing
  1. Sampling basics and challenges
  2. CONTROL, Blink, Sample-and-seek, AQP++
* Streaming
  1. Windowed Streaming
    * DataFlow paper
    * CQL/Stream project
    * TelegraphCQ
  2. Complex event processing
    * SASE
* X in DBs
  * ML in SQL
    * MADLib
    * SystemML
    * Learning over joins
  * Graph in SQL
    * Jignesh's papers
    * Vertexica
    * RecStep
  * Vis in SQL



<!--

Topics will cover a subset of papers from [the redbook](http://www.redbook.io), as well as modern provenance/lineage, data analysis, cleaning, and perhaps databases+ML.


* Intro
  1. Syllabus + life of a query + meta stuff
    * Codd
  2. DB primer/background
    * Storage hierarchies and [numbers you should know](https://gist.github.com/hellerbarde/2843375)
    * The importance of simple equations
    * 5 minute rule
    * Other principles
* Basics
  1. [Architecture of a DB](http://db.cs.berkeley.edu/papers/fntdb07-architecture.pdf)
  2. [SystemR retrospective](http://db.cs.berkeley.edu/cs262/SystemR-annotated.pdf) or   
     [Design of Postgres](http://db.cs.berkeley.edu/cs286/papers/postgres-cacm1986.pdf)
* Indexes
  1. R-trees
  2. [GIST-trees](http://db.cs.berkeley.edu/papers/vldb95-gist.pdf)
* Joins
  1. Shapiro: Join Processing in Database Systems with Large Main Memories  
  2. Track Join (Wangda?)
* Execution
  1. Volcano's Exchange
    * https://people.eecs.berkeley.edu/~brewer/cs262/exchange+eddies.html
  2. Eddies
* Lower level Optimizations
  * DBMin
  * [Hybrid Caching](http://db.cs.berkeley.edu/cs286/papers/caching-sigmod1996.pdf)
* Query Plan Optimization
  * Classics
    * Selinger
    * Cascades
    * Volcano Optimizer
  * Modern stuff
    * Using RL for join optimization
* Languages
  1. datalog
  2. schemaSQL
* Systems Architectures
  1. C-Store
    * Column-Stores vs. Row-Stores: How Different Are They Really?
  2. H-store/Hekaton
* Systems Architectures
  1. Query Compilation
    * T. Neumann, Efficiently Compiling Efficient Query Plans for Modern Hardware
    * K. Krikellas, et al., Generating Code for Holistic Query Evaluation, in ICDE, 2010
    * How to Architect a Query Compiler, Revisited
  2. ??
* Materialization for physical database design
  1. Materialized Views
    * Updating Materialized Views
    * Surajit's paper
      * http://www.vldb.org/conf/2007/papers/special/p3-chaudhuri.pdf
  2. Datacubes
    * Jim Gray paper
    * [Implementing data cubes efficiently](http://db.cs.berkeley.edu/cs286/papers/datacube-sigmod1996.pdf)
* Approx Query Processing
  1. Sampling basics and challenges
  2. CONTROL, Blink, Sample-and-seek, AQP++
* Streaming
  1. Windowed Streaming
    * DataFlow paper
    * CQL/Stream project
    * TelegraphCQ
  2. Complex event processing
    * SASE
* X in DBs
  * ML in SQL
    * MADLib
    * SystemML
  * Graph in SQL
    * Jignesh's papers
    * Vertexica
* X in DBs
  1. Vis in SQL

-->
<!--

* Distributed Query Processing
  1. Gamma: distributed Joins
  2. 
* Concurrency Control
  1. Serializability, Linearizability, tec overview
  2. MVCC and OCC
* Basics of Plan Execution / optimization
  * SEDA?
  * dbmin
* Languages
  * SchemaSQL
  * datalog
* Storage
* Recovery
  * ARIES
  * H-store
* Architectures
  * C-Store + ten years later
  * Hekaton
  * MR/Spark
  * Naiad
  * Query compilation + Tarik
* Concurrency Control
  * MVCC vs OCC vs Pessimistic vs CALM
* Slightly modern stuff
  * In network execution?
  * ML in SQL
    * MADLib
    * SystemML
  * Graph in SQL
    * Jignesh's papers
    * Vertexica
* Scheduling
* Networking
-->
