---
layout: page
title: W6113 Research Project
---

<style>
.cool {
  background-color: steelblue;
  color: white;
  text-weight: bold;
}
</style>

### Important Dates 

Percentages are of your total class grade.

* Proposal    10-01   (5%)
* Paper Draft   10-29  (10%)
* Presentation  12-10  (10%)
* Report        12-14   (40%)



### Overview

The major portion of your grade is based on the research project. Students will organize into teams of 2-3 students and work on a research project.  It should take about 3-4 weeks to complete.  Some possible ideas are [described below](#suggestions).

Teams should consist of 2-3 people (we may adjust this depending on the size of the class). In addition, if you have a project in mind, please discuss it with Eugene well ahead of time. We have also included a list of possible projects at the end of this document although you are not required to choose from these.

Good class projects can vary dramatically in complexity, scope, and topic. The only requirement is that they be related to something we have studied in this class and that they contain some element of research -- e.g., that you do more than simply engineer a piece of software that someone else has described or architected. To help you determine if your idea is of reasonable scope, we will arrange to meet with each group several times throughout the semester.

Choosing a research problem is very difficult, especially if you have not done so before.  You may end up thinking of, and discarding many possibilities before finding the project you ultimately work on.  Have a fuzzy idea?  Want some feedback or help brainstorming a project?  **Come to office hours and/or recitation.  The staff are all here to help!**


<a name="proposal" />
### Proposal

Your research proposal will contain an overview of the research problem, _your hypothesis_, first pass at related work, a description of how you plan to complete the project, and metrics to decide _if it worked_.   


We have setup a template for your proposal on overleaf.  Clone it into your team's account to edit it.  Make sure to change the title and author names, and include your team members' UNIs.


**Submission**

1. Use the [proposal template on Overleaf](https://www.overleaf.com/read/xhpgqyqbghry)
1. [Click here to submit](https://www.dropbox.com/request/4twBRI2OeuplW2rSV4Ih)




<a name="draft" />
### Paper Draft

You will submit a draft of your paper that should be between 4 -- 6 pages. Please use the [overleaf report template](https://www.overleaf.com/read/phmrptrtjrhz) to get started.  It already contains a scaffold of sections, and suggestions of what to include in each section.  Your report is not beholden to these sections, so take the template as a starting point.  

For the draft, you should have a fleshed out introduction, related work, and technical overview.  You should have a clearer idea of the technical details than from the proposal, but need not have implemented it yet.  You do not need to have run experiments yet, but should sketch out the hypotheses and the potential experiment setup (which may change). If you have preliminary findings, that's great!  Please include those.

In short, I expect that you have a much clearer idea about the problem _and_ how it can be solved.  Most of the technical details and relevant work should be clear, but you may not have implemented it yet.


Tips:

* [Tips for Writing Technical Papers - Jennifer Widom, Dean of Stanford Engineer](https://cs.stanford.edu/people/widom/paper-writing.html)

**Submission**

1. Use the [report template on Overleaf](https://www.overleaf.com/read/phmrptrtjrhz)
1. [Click here to submit your **4 -- 6 page** draft](#)



### <a name="showcase"/>Project Showcase 

Your team will prepare and present a project poster at the end-of-course showcase session.   This gives you an opportunity to present a short presentation demo of your work and show what you have accomplished in the class!  

Your presentation should be polished.  Since there is still time until the final report, you are encouraged to also discuss ideas or challenges you are still considering.  

**Since you are presenting to your peers as well, make sure you give your colleagues enough context to understand your ideas.  In addition to _what_ you did, help your colleagues understand _why_ you made your specific choices, and provide examples.  It's better to make sure the audience learns a few specific ideas than try to say everything.**  Come to office hours or contact the staff if you would like feedback.

Overall logitics

* 2 person teams: 6 min presentation, 5 min feedback
* 1 person teams: 5 min presentation, 4 min feedback
* Timing is strict since we have many groups.  *Practice ahead of time so your presentation is smooth!  Only takes 5/6 minutes per practice :)*
* Each team member should speak
* Make sure all demos are embedded as GIFs or videos in your slides.
* Staff will host and share their screen; we will change slides on your behalf

Your presentation should cover (in content, not necessarily one slide for each point)

* Motivation and *scientific hypotheses*
* Technical challenge and contribution
* Related work and how they are related
* Simple example to illustrate idea
* Technical insights/experimental findings so far
* GIF/video of demos/screenshots (if applicable)
* Feedback: 1-3 questions you’d like feedback on

**Submission**

* Submit URL to your group's [PDF file or google slides](#)



### Report/Camera Ready

You will revise your draft and submit a conference-style report on your project, with **maximum length** of 12 pages. 
Because this report is the primary deliverable upon which you will be graded, **do not treat it as an afterthought**. Plan to leave at least a week to do the writing, and make sure your proofread and edit carefully!

**Submission**

* [Submit here](#) 


<a name="types"></a>
## Project Types

There are two broad categories of projects, the Reproduce and Extend Project, and the Research Project.

#### Reproduce and Extend

The goal of this type of project is to deeply understand how an existing problem is solved, and then slightly improve it.
Once you pick a problem (basically, pick anything we mentioned in class, or any component of a system), read the literature to understand
the different ways it has been solved.  This should require doing a literature search by using Google Scholar, surveys, and following citations.
You should expect to read 5-10 or more papers, and to summarize them in your related works section.

Since the best way to understand something is to implement it, you will then pick the best-in-class approach from your readings 
and implement it in a system.  For a database algorithm or component, DataBass may be sufficient, or you may choose some other system.
You will then benchmark your implementation and report on the results.

After coding, debugging, benchmarking, debugging, laughing, crying, debugging the approach, you should be intimately familiar with the problem.
At this point, introduce an improvement.  This can be a special case for a particular class of queries or data distribution, or exploiting a 
hardware optimization, or leveraging some special property of a use case.  Once you implement the improvement, update your benchmarks and 
explain the results.

The final report should still be the same structure.  Naturally, the introduction will focus less on novelty, and more on how the system that you modified did not 
take advantage of your implementation, and the motivation behind your improvement.   In contrast, your related work will be a detailed history and account of
how this problem has been solved in the past and their pros and cons.


#### Research Project

The goal of this type of project is to identify a new problem, propose an algorithmic solution, and evaluate and report the findings.
Its primary difference from the previous type of project is that it starts from a novel problem and seeks to solve it using whatever means make sense, 
whereas Reproduce and Extend Projects start with an established problem and solution.

The key challenge for this type of project is to establish novelty.  To do so, there should be _some_ example of your project that prior work cannot
easily solve with some minor tweaks.  

There are many sources of potential research projects.  Here are some ideas:

* You may have encountered some data management problem and could not find a satisfying solution.  
* You have an idea about something useful that _should_ be easily doable, but is painful or impossible with current state of the art.  
* There are too many approaches to solve a problem and it's not clear which one to use under what conditions.  Run a bake-off and evaluate.
* You did a Reproduce and Extend Project, and found that the approaches don't actually work in real scenarios.  Make it work


<a name="suggestions"></a>
## Project Suggestions


### Reproduce and Extend

Many of the following can be done by extending Databass' functionality

Worst Case Optimal Joins

* Read the literature on worst case optimal joins, and integrate it into DataBass (including extending the optimizer to choose it when applicable).

Compilation

* Extend Databass to generate rust or asm.js, or a custom IR.

Columnar

* Extend the Databass execution model to operate over columnar chunks such as Apache Arrow.
  Bonus for late materialization or bitmapped execution.

Lineage summarization

* There's some interesting research on lineage summarization.  Extend Databass' lineage capture mechanisms
  to automatically summarize/approximate lineage during capture.

Incremental computation ala DBToaster

* Extend Databass to perform incremental computation, where a standing query incrementally maintains its results as data streams in (say, via a scan)
* Bonus points if it incrementally maintains the lineage indexes as well!

Access Methods

* Databass only supports scans.  Extend Databass with different access methods and extend the optimizer to recognize and use those access methods.

<!--
Benchmarking

* benchmark vega and diff dataflow, find benchmarks
-->



### Research Projects

The following are potential research projects.  Read the relevant papers and come to OH if you are interested in any of them.


#### Lineage

##### Lineage Capture for Pandas

Fine-grained lineage is very useful, and [Smoke](https://arxiv.org/abs/1801.07237) is the fastest lineage capture engine.
Unfortunately, it's not a full query engine and no one uses it.  Everyone does, however, use Pandas.  

IDEA: Is it possible to efficiently capture fine-grained lineage in Pandas (or with a pandas compatible API)?

* Solving this fully is not realistic, but it is feasible to perform a feasibility study.
  For instance, hand instrument a few Pandas operators to understand what would be needed to
  instrument the rest of the library.  Benchmark those operators and understand where the
  overheads come from.

##### Lineage for Optimizing Query Execution

The [Smoke paper](https://arxiv.org/abs/1801.07237) described several workload aware optimizations that leverage
lineage capture to build data structures that benefit later queries.  This form of "adaptive" query optimization
is a neat idea.  Of course, capturing lineage incurs a runtime and storage overhead, so it is not free.  Further,
the examples in the paper were hand-written feasibility studies, so the query optimizer is not actually aware of
the lineage-based data structures.  

IDEA: Extend DataBass to support and manage lineage-based data strutures:

* Design a low-overhead resource management module that turns off lineage capture once its runtime or storage
  overhead exceeds some threshold.  The threshold could be per-query or database-wide
* Extend the lineage capture logic to generate workload-aware lineage data structures, instead of or in addition to
  the existing lineage indexes.
* Bonus: extend the optimizer to use these data structures.


##### Applications of Fine-grained Lineage

Lineage is typically used for a small set of well defined use cases: [visualizing the lineage](https://www.cs.ubc.ca/~mkmilani/pastwatch.pdf) as a [node-link graph](https://web.cs.ucdavis.edu/~ludaesch/pubs/Provenance-Browser-ICDE-2010.pdf)
[debugging](http://www.vldb.org/pvldb/vol9/p216-interlandi.pdf), [view updates](https://d1wqtxts1xzle7.cloudfront.net/42047143/Provenance_in_Databases_Why_How_and_Wher20160204-16814-ky9amz.pdf?1454595616=&response-content-disposition=inline%3B+filename%3DProvenance_in_Databases_Why_How_and_Wher.pdf&Expires=1599740653&Signature=IOywJW9BodOgh9opL09WgM3Q5Iri4ZoSI46~JvlbvO1bMa7f7HMExc67ySNshhv07iCFXVA2-Fhis6LZ-iSXYfqtozohw49uqC8JM0c7FynZLOsRuQqyHVZFT82MvJITWy1cLWdx6fo5EsKMEmdao66T4FX1fPvwfS2rG5Qkf8ujoC8t6TIy1ZdZVffbCJ3sqcfMrwULMzOgkYZJQMtIi9GUcAd4tZ40KkyvlC6Xa~JmDRXBtenCJatuTzm45X2hz3TGqZubfaxyI8pHi1yLBqnqVkeMiFgIgM0ldW9MrJyzcBfUjhG1aG5aYGNx0991IVnRqZQji9Pnw9kwUG6cBA__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA),
responsibility.  Explore alternative uses of lineage.

IDEA 1: Most people interact with data through a visualization that cleary defines how its axes map to attributes 
  in the rendered data; the rendered data may be a query result.  When the user points to bars and circles in
  the visualization, lineage tells us what the inputs are.  Is there a way to leverage the query and visualization
  automatically choose a good way to render the lineage?

IDEA 2: The [Smoke HILDA paper](https://www.dropbox.com/s/fkp5hk1gp4lrg9h/smoke-hilda18.pdf?dl=0) outlined how
  lineage could be used to make implementing interactive applications easier. It mainly said that it 
  "should be possible", but didn't flesh out the actual library.  Recommend a potential library by building out
  a practical use case and reporting on the lessons learned.  

* One use case is linked visualization.
  Linked-visualization refers to the ability to interact with data in an chart, and update the other charts to reflect the selected data.
  [Crossfilter is a popular example](https://square.github.io/crossfilter/), but is limited to simple count-aggregation queries. 
  Design a dashboard system that lets the user submit and visualize multiple SQL queries; extend DataBass' lineage system
  to automatically support linking between any of the visualized results.


#### Querying and Access Methods

##### Query Language and Execution Pushdown for DiffParsing

A common way to analyze query logs and evolving code bases is to study how the queries/programs change over time.
This is typically done by parsing the queries into ASTs, and then comparing tree differences between queries. 
Suppose there are N queries, then this requires parsing the N queries, and then an N^2 pairwise tree alignment.

DiffParsing is an existing project that combines tree differencing into parsing.  The idea is that divergences
during parsing are exactly the points where the resulting ASTs will be different, so there is no need for a
separate alignment step. There is an implementation of the core DiffParsing algorithm.

IDEA: Design a query language over the dataset of tree differences, and show that it can be applied to interesting use cases.

* This language should at minimum support filters and aggregations.
  Then implement optimizations that push as much of the query into the DiffParsing algorithm as is efficient,
  to avoid unnecessary materialization.


##### Reality Access Methods

[RealitySketch](https://ryosuzuki.org/realitysketch/) is an amazing HCI project, watch its video.
From a database perspective, their project turns ipad video annotations into an access method _of the real world_.
When they circle the pendulum, it turns into a table with schema (time, angle, x, y).  


IDEA 1: in an image or video containing many objects of the same type (balls, forest, crowd),
enable the ability to highlight an instance of the object, parameterize it, and then query the entire scene/video.
The way RealitySketch does this is by sketching on the ipad and specifying how the scene should be parameterized (see paper),
but other methods are possible.
One approach could be

* Use realitysketch's method, or use one-shot learning to train an object detector
* Apply detector to rest of image/scene/video
* Extract parameters from detected objects
* Expose query interface

IDEA 2: make it incredibly easy for normal users to create new "reality access methods", and to be able to
query over these access methods.  These access methods could be based on phone sensors, video, audio, touch screens, wireless signals, etc. 







#### Progressive Computation and Khameleon


[Khameleon](https://medium.com/thewulab/for-responsive-interactive-apps-prediction-is-not-enough-3188bc7b53db) ([video](https://www.youtube.com/watch?v=oiU5xytHMm4)) 
is a project that masks communication latencies for cloud-based interactive applications.  To do so, it leverages progressive encoding
by prefetching very little data for less likely requests, but lots of data for the most likely requests.

##### Progressively encoded cubes

Progressive encoding transforms a data item into a sequence of bytes where any prefix is an approximate result.
JPEG is an example of progressively encoded data, a few bytes shows a low quality image, and adding a few more bytes improve the quality.
Similarly, a breadth-first ordering of a secondary index is a progressive encoding -- larger prefixes correspond to a deeper tree that is more effective at filtering.

IDEA: Is it possible to compute and return a progressively encoded data cube, where larger prefixes correspond to finer granularities for the useful dimensions?
  In other words, can you devise an algorithm that returns a progressively encoded data cube in less time than computing the cube and then encoding it?
   
##### Interactively Explore 1M+ images

The Khameleon paper was evaluated on an application that explores 10K images, however large image datasets contain 1M+ images, stored on scalable but remote services like EC2.
In [the extended technical report](https://arxiv.org/pdf/2007.07858.pdf), Figure 16 shows that Khameleon's greedy scheduler does not scale well as the number of possible requests increases.
This is primarily because of inefficiencies in how the scheduler interacts with the prediction distributions.

IDEA: Extend Khameleon's predictor and scheduler to circumvent these inefficiencies, and build a demo that can explore 1M+ images.   There are many massive image corpi that this would be very useful for.
Read the paper and then talk to Eugene in OH.



#### ML+Systems

##### Orchestrating Learned Components

Systems are increasingly using learned components to automatically make local optimization decisions.
A learned index examines the sequence of reads and writes to decide how to optimize its internal layout.
A workload optimizer examples the sequence of queries to decide how to optimize the database layout.
A learned buffer pool manager may see the sequence of page accesses to decide on the replacement policy.

The challenge is that the sequence of data available to the learned component is too low level.
In the database, upper layers constantly communicate with lower layers.
the choice of join algorithm (in the executor) is used as a hint to the buffer pool replacement strategy.  

IDEA: A learned component can be modeled as RL to decide policies that change the component.
  Can useful features from one part of a system improve the effectiveness of a learned component?
  This project would test the feasibility in several stages.  

1. Find a learned index.  Show that by adding hand crafted informative features that upper layers
   of the database would know, it can be used to improve the model's forecasting accuracy.
  Ideally, it does not require mucking with the internals of the RL model.
1. Show that a mixture of informative and uninformative features can still be effective..
1. Show that this actually improves the performance on serial workloads (one query, then another).
1. Show that this actually improves the performance on concurrent workloads (query accesses are interleaved).

Informative features could come from

* The application interface.  For instance, when a user hovers over a button that will trigger queries that use the index.  The feature could be the hover event.
* AST/query plan features (such as predicate values) known before the query actually runs.  
* Physical operators chosen by the optimizer.  


##### Benchmarking Workloads

A benefit of learned DB systems is that they evolve with the workload, thus a good metric is how quickly
a learned DB can adapt to a new workload and achieve good performance.
However, what is a good "evolution workload" to evaluate learned DB systems on?
It's hard enough to create benchmarks like TPC-H/DS for non-learned databases.  

IDEA: use schema matching to adapt the query workload from an existing benchmark to
run on the dataset of another benchmark.  For instance, we would like to run the TPC-H
query workload on the TPC-DS dataset.  In this way, we can measure how quickly a learned DB
transitions from a TPC-DS workload to the "mapped TPC-H" workload.
This can be very useful for the Learned DBs field.
Creating an evolved benchmark requires several steps:

* Apply schema mapping from benchmark 1's dataset to benchmark 2's dataset.  There may be multiple valid mappings.
* Use a valid mapping to map benchmark 1's queries to benchmark 2's dataset.
* Profit (actually, run a few database systems on the evolved benchmark).




<!--

rain

IFC for concurrency control

-->
