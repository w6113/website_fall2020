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

* Prospectus      2/14    (10%)
* Paper Draft     3/22    (5%)
* Mock PC         4/2, 4/4  (5%)
* Presentation    4/30    (10%)
* Report          5/10     (40%)



### Overview

The major portion of your grade is based on the research project. Students will organize into teams of 1-3 students and work on a research project.  It should take about 3-4 weeks to complete.  Some possible ideas are [described below](#suggestions).

Teams should consist of 1-3 people. In addition, if you have a project in mind, please indicate briefly (1--2 sentences) what you are thinking. We have included a list of possible projects at the end of this document although you are not required to choose from these.


Good class projects can vary dramatically in complexity, scope, and topic. The only requirement is that they be related to something we have studied in this class and that they contain some element of research -- e.g., that you do more than simply engineer a piece of software that someone else has described or architected. To help you determine if your idea is of reasonable scope, we will arrange to meet with each group several times throughout the semester.

<!--
#### Proposal Presentations 

At the beginning of the 2nd to 4th lectures, each group will give a **5 minute presentation** about their proposed project to the class.  The presentation should contain:

* Project idea and hypotheses
* What work must be done and how it will be diveded amongst the team
* How the hypotheses will be evaluated
* Resources needed to complete project

Teams can meet with the instructor after their presentations for further discussion and feedback.

[**Click here to sign up**](https://calendar.google.com/calendar/selfsched?sstoken=UUlmUlc5VDIwWDJwfGRlZmF1bHR8MTUwY2E3NDBiMDNhMTU4ZDIyODhlMjFlZTAzZGMyZTU).  Click "next" until you get to the appropriate week.
-->



<!-- [Click here to submit before class on 2/1](https://goo.gl/forms/j8aXKKtjxH0rzVgx2) -->


### Prospectus 

Your research prospectus will contain an overview of the research problem, _your hypothesis_, first pass at related work, a description of how you plan to complete the project, and metrics to decide _if it worked_.   

Your prospectus should follow the example:

* [Click here for an example prospectus](./files/prospectus/prospectus.pdf)
* [Click here for the tex files](https://github.com/w6113/w6113.github.io/tree/master/files/prospectus)

**Submission**

1. Rename the filename of your prospectus to the following format, last names should be in **alphabetical order**. `prospectus_<UNI>_.._<UNIn>.pdf`
2. [**Click here to upload the file by 2/14 11:59PM EST**](https://www.dropbox.com/request/Opyk8ALWnSyYEin0ZHKs)


<a name="midpoint"></a>
### Mock PC Meeting and Paper Draft

We will spend two class sessions running a mock program committee (PC) meeting.  The timeline for this will be as follows:

* **3/22 11:59PM EST** Submit a draft of your paper to CMT **[using the ACM proceedings LaTeX template](https://www.acm.org/publications/proceedings-template)**.   The draft should be a fleshed out version of your prospectus, with substantially more technical details and a sketch of your experiments.
* **3/23** You will be assigned 3-4 papers to review, and serve as the "lead" for one.  The review format will be the same as the reviews throughout the semester.
* **3/29 11:59PM EST** You will submit your reviews to CMT.   Read the other reviews for your assigned papers over the weekend.  
* **4/2 - 4/4** We will discuss each paper based on the reviews (authors will step out of the room).  Each reviewer will argue their view on the paper, and try to reach a consensus.  The lead is responsible for running the discussion.   The lead will also summarize the discussion/outcome into a meta review.  

#### The Paper Draft

Your paper should be no more than 10 pages, and include at least the following sections:

1. Introduction: motivate the problem, summarize related work, and declare your crisp hypothesis (or hypotheses).  This should be fully present.
2. Related Work: describe the state of the art in the most relevant research areas to your project.  This should be fully present.
3. Technical Overview: outline the technical approach you are taking so that the reader has an intuition about the solution.  This should be fully present.
4. Technical Details: considerably more technical details of your project, and details on what has been implemented.  The details should be mostly complete, but may not be implemented yet.
5. Experiments: describe the experimental setup as we have gone over in class.  You may not have run experiments yet.  If you have, feel free to include them.

In short, I expect that you have a much clearer idea about the problem _and_ how it can be solved.  Most of the technical details and relevant work should be clear, but you may not have implemented it yet.

**Submission**

* [CMT website](https://cmt3.research.microsoft.com/w6113).  MAKE SURE YOU USE THE CORRECT TEMPLATE.


#### Paper Reviews

Paper reviews address the same points as the roles that we have been focusing on.  They are different in that you want to propose concrete points that are great, and points that can use improvement.  Beyond that, study suggestions on how to review, and NOT review, papers:

* [Review AntiPatterns (written for FSE 14 PC)](https://homes.cs.washington.edu/~mernst/advice/review-antipatterns-devanbu.txt)
* [Ethics of Peer Review](https://ori.hhs.gov/sites/default/files/prethics.pdf)
* [How NOT to review a paper](https://sigmodrecord.org/publications/sigmodRecord/0812/p100.open.cormode.pdf)
* [Conference Reviewing Considered Harmful](https://homes.cs.washington.edu/~tom/support/confreview.pdf): A view on how reviewing works in practice.


#### PC Meeting

Preparation

* Read the reviews for each paper, including papers you did not review
* Prepare to share your perspective on each paper.


For each paper, we will choose one or more of the reviewers as the "Shephard".  Their job is to:

* Lead the discussion during the PC meeting
* Work with the individual reviewers to ensure that the reviews are complete, positive, constructive, and reflect the discussion.
* Work with the authors during the rest of the semester to ensure that the final version of the paper meets the standards from the PC discussion.
* In short, the paper's success is tied to the Shephard's success.

PC Meeting Format

* We will discuss half the papers in each lecture.
* Authors of the discussed paper will leave the room.
* PC will discuss the paper, along the dimensions that your review roles have been focusing on, and agree on feedback to provide authors
* Shephard will write a summary review emphasizing the main points for the authors
* Each reviewer will update their own reviews based on the discussion.  This can involve removing points, adding new comments, clarifying points, etc
* Shephard works with reviewers to ensure reviews are constructive.  
* Reviews are released day after the PC meeting at the latest.

Paper Discussion Format

* Shephard leads the discussion.  
* Reviewers summarize their overall impressions, then broader discussion about the merits of the work
* All reviewers and PC members have equal standing
* Shephard keeps the discussion on track, and keeps time.

<a name="shepherd"/>
#### Shepherd Duties after PC Meeting

* Go over all reviews for shepherd'd paper and ensure they are positive, detailed, and constructive.
* Write summary review, and get sign off by reviewers.
  * Summary review should be written in Details box of your review, under a heading such as 
  
        -------- SUMMARY REVIEW --------

* Discuss with paper authors in person to clarify review suggestions.


<a name="reflection"/>
#### Post-PC Meeting Reflection (Due Sat 4/6 11:59PM)

[Use this form to submit](https://forms.gle/wmqKEU1AW4bMs3G4A)

Reflect on your own reviewing

1. For each paper you reviewed:
  * What are the top 3 or more ways in which your review is similar to the other reviewers?
  * What are the top 3 or more ways in which your review is different to the other reviews?
2. Overall, what are takeaways or lessons from this process that you can apply when you write reviews in the future?

Submit a reflection of your project

* How can you improve the motivation/introduction (if applicable)?
* How can you improve the technical ideas (if applicable)?
* How can you improve the evaluation (if applicable)?
* How can you improve the writing and argumentation (if applicable)?
* How useful were the reviews?






<!--
#### Poster Session (TBA)

Your team will prepare and present a project poster at the end-of-course poster session.   This gives you an opportunity to present a short demo of your work and show what you have accomplished in the class!

**Submission**

* Simply attend and present at the poster session.

-->

### Report/Camera Ready (5/10 11:59PM EST)

You will prepare a conference-style report on your project with **maximum length** of 12 pages (10 pt font or larger, one or two columns, 1 inch margins, single or double spaced -- more is not better.) Your report should expand upon your prospectus and introduce and motivate the problem your project addresses, describe related work in the area, discuss the elements of your solution, and present results that measure the behavior, performance, or functionality of your system (with comparisons to other related systems as appropriate.)

Because this report is the primary deliverable upon which you will be graded, **do not treat it as an afterthought**. Plan to leave at least a week to do the writing, and make sure your proofread and edit carefully!

**Submission**

* [CMT website](https://cmt3.research.microsoft.com/W61132019/) by 5/10 11:59PM EST

<!-- [**Click here to upload the file by 5/2 11:59PM EST**](https://www.dropbox.com/request/9zdikb92vHFFPYtaFF0e) -->


<a name="suggestions"></a>
## Project Suggestions

The following are examples of possible projects -- they are by no means a complete list and **you are free to select your own projects**.  In fact, a common source of ideas is to take your experience from another domain, and combine it with databases/data management.  Projects often come in several flavors:

0. Make DataBass better: extend DataBass in a significant way, and evaluate it against other systems.  For instance, support DSM/PAX, distributed execution, LLVM compilation, lineage, etc.  Code quality matters for this option.
1. Research project: model an unsolved problem, propose algorithmic solution, evaluate and report findings.
2. Win: pick an existing useful application and a well-recognized metric (latency, prediction, etc) and win against the state of the art.
3. Break and fix: implement a state of the art algorithm on real data, show that it doesn't actually work (results are poor, it's slow, etc), make it work.
4. Evaluate: there are many options out there, it's not clear which ones are actually best, and under what conditions.  Run a bake-off and evaluate.
5. Fill a gap:  think about something useful that _should_ be easily doable, but is painful or impossible with current state of the art.  Fill that gap.


#### Precision Interfaces

[Precision interfaces](https://www.dropbox.com/s/bac9qjz0s5m4kpx/precisioninterface-sigmod19-v2.pdf?dl=0) analyzes query logs and generates custom interaction components from the logs.  The goal is to scalably generate dozens or hundreds of custom interactive analysis interfaces for any analysis found in a log.    

* Precision interfaces is currently language agnostic and does not take into account the database nor the database contents.   Adapting the system to make weak but general assumptions about the nature of query plans, data, and query results can potentially improve the usability and usefulness of the generated interfaces.  
* Embed design heuristics into the interface generation process.  The system currently has a very simple model of "interface complexity" --- make it more real by taking existing HCI research into UI complexity and design into account.

#### Deep Neural Inspection

[DeepBase](https://medium.com/thewulab/deep-neural-inspection-with-deepbase-de3653257643) is a system to perform deep neural inspection: it extracts hidden unit activations (or other types of behaviors) and computes the statistical relationships with user-specified hypotheses.    

* Idea 1: Use ideas from class to make the system scalable across a cluster of machines.  
* Idea 2: Hypotheses are currently represented as independent vectors/matrices and processed one at a time (essentially).    Since most hypotheses are binary or have a restricted value range, there may be opportunity for bit-level packing and shared processing.  


#### Lineage 

[Smoke](https://www.dropbox.com/s/6xvg5qkdret60jk/smoke-vldb18-revision.pdf?dl=0) is the fastest lineage-enabled database engine.  It captures the relationships between output and input records as efficient lineage indexes.  It turns out, this can be used to express and speed up interactive applications such as visualizations.  Extend or use it in interesting ways 

* There are a number of compression techniques that are possible to reduce the storage costs, but they have trade-offs in terms of storage reduction vs write overhead vs lineage query lookup costs.  Explore ways to generate compressed representations that do not increase, or even reduce the overhead of lineage capture.
* [Smoke](https://arxiv.org/abs/1801.07237) is a query compiler instrumented to generate lineage.  It is written in C++, and emits C++.  If the goal is to compile queries into C++ (or C), a high level language like Python may be easier to program in.  Report on the benefits (or weaknesses) of using a high-level dynamic language to write a query compiler.  Python interoperates well with C -- are there opportunities to dynamically compile queries into C and link it into the same Python process?
* The [Smoke HILDA paper](https://www.dropbox.com/s/fkp5hk1gp4lrg9h/smoke-hilda18.pdf?dl=0) envisioned a world where any interactive applications built on top of a lineage-supporting data store can inter-operate with any other application.  No longer are applications siloed!  Data selected, analyzed, and annotated in any application should be connected to any other application!  This requires connecting the core functionality in Smoke with application level lineage support and tracking.  Is there a simple app toolkit/library, with a small set of primitives, that could make it easy to build applications that enable this vision?  Is something like react or elm a good fit?


#### New Querying Interfaces

[Scalable](https://www.microsoft.com/en-us/research/uploads/prod/2019/01/Wu-drucker-QueryingVideos.pdf),
[Image](http://cidrdb.org/cidr2019/papers/p141-kang-cidr19.pdf),
[Databases](http://cidrdb.org/cidr2019/papers/p40-krishnan-cidr19.pdf) are on the horizon.  However, a major limitation is that the query interface is incredibly impoverished.  How do you specify that you want to find red cars that move along a trajectory?  Or to look for relationships between two objects over time?  Certainly not by writing SQL-like text queries.   The challenge is that video is fundamentally 3D, but query interfaces are 1D.  

* Idea 1: the core abstraction in relational algebra is Joins.  In video, it is likely also joins, but for the same image across video frames, or the relationship between objects across video frames.  The nature of trajectories, positioning, and timing are all core aspects to relating concepts in video.  Propose and implement a prototype to help users express video joins.
* Idea 2: VR can render videos as 3D objects.  What does a query language look like if designed for VR?  What types of joins, or filtering, make sense?  You should have VR experience.   

#### In-Network Query Processing

Contact Arpit Gupta if interested: glex.qsd@gmail.com

To keep the networks running, network operators need to monitor a wide range of network activities. For example, they need to concurrently detect whether the network is under attack and also determine whether there is a device failure in the network. This involves extracting multiple features from the traffic data and combining them to infer network events in real time. 

[Sonata (SIGCOMM’18)](https://sonata.cs.princeton.edu/) is an expressive and scalable telemetry system that coordinates joint collection and analysis of network traffic. Sonata provides a declarative interface to express a wide range of common telemetry tasks as dataflow queries. To scale execution, Sonata partitions each query across the programmable switch (e.g., [Barefoot Tofino](https://barefootnetworks.com/products/brief-tofino/)) and the stream processor---offloading as much data processing as possible to the switch. To optimize the use of limited switch memory, Sonata dynamically refines each query over time to ensure that available resources focus only on traffic that satisfies the query. 

Possible directions:
* **Scalable and adaptive query planning**: Currently, Sonata’s query-planning module takes raw packet traces as input and then executes the input queries for all possible refinement and partitioning plans to estimate their memory requirement and compute overhead. It then takes these estimates as input to compute the optimal query plan using an integer linear program (ILP). This approach is not scalable as the number of queries or the size of input packet traces increases. Also, it assumes that the input packet traces are representative of the future traffic. This assumption leads to inefficient utilization of limited network resources as traffic patterns change over time. Thus, students can explore the design of a query-planning algorithm that scales better and is adaptive to changes in traffic dynamics.
* **Efficient query compilation**: Currently, Sonata compiles a DAG of dataflow operators for a query into DAG of match-action tables (MATs) in the switch. The compiler needs to specify the memory required for the stateful operations during the compilation. Reconfiguring the switch is expensive, so currently, it is not possible to dynamically update the memory allocation for stateful operations over time. Thus, students can explore the design of new data structures and compilation algorithms that enable dynamically reallocating switch resources (memory) for different queries over time. 
* **Query-planning for network-wide settings**: Currently, Sonata is only designed for a single site in the network, such a border router or an Internet exchange point. Students can explore the design of a system that executes network telemetry queries for network-wide settings---partitioning and refining the input queries across multiple switches in the network. 

#### Query-based Graph Visualization

Graphs are fundamentally high dimensional, and generating good graph visualizations is still an unsolved problem.  There are plenty of ways to visualize a graph---as a matrix, as a node-link layout (with many mayn layout algorithms), as histograms, and so on.  Suppose you know what analysis _queries_ (e.g., recursive SQL queries, or a query workload) have been run on the graph.  Can those queries be analyzed to recommend the appropriate visualization?

#### What We Talk About When We Talk About Data

How are data and analyses referred to and described in scientific work?  When data is presented as figures or tables, how is it referred to?  What are the verbs and nouns?  Is there a universal set of ways that figures are described (e.g., in terms of comparisons? in relative terms? ).  This can serve as the evidence for a new data analysis language.  Analyze [Viziometrics](http://viziometrics.org/api/) and ArXiV for their figures and captions and surrounding text (ArXiV provides LateX files)

<!--
#### Bake-off

There are more and more database implementations popping up from big companies: [uber](https://eng.uber.com/aresdb/),   

-->



<!--


#### Data Cleaning

Understand how scientific articles use and talk about data.  Two possible directions:

Arachnid is a new explanation engine that automatically generates cleaning programs based on user specifications of data quality.  It is an extension to ideas from [Scorpion](https://www.dropbox.com/s/1v6dcb16r840sdo/scorpion-vldb13.pdf?dl=0).  Contact Eugene for a copy of Arachnid.  Some possible projects:

* Integrate Arachnid into an interactive data exploration interface in a way that the user can clean any part of a visualization without programming
* Implement a fast version of Arachnid in the browser



-->




