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

The major portion of your grade is based on the research project. Students will organize into teams of 1-3 students and work on a research project.  It should take about 3-4 weeks to complete.  Some possible ideas are [described below](#suggestions).

Teams should consist of 1-3 people (we may adjust this depending on the size of the class). In addition, if you have a project in mind, please indicate briefly (1--2 sentences) what you are thinking. We have included a list of possible projects at the end of this document although you are not required to choose from these.


Good class projects can vary dramatically in complexity, scope, and topic. The only requirement is that they be related to something we have studied in this class and that they contain some element of research -- e.g., that you do more than simply engineer a piece of software that someone else has described or architected. To help you determine if your idea is of reasonable scope, we will arrange to meet with each group several times throughout the semester.

Choosing a research problem is very difficult, especially if you have not done so before.  You may end up thinking of, and discarding many possibilities before finding the project you ultimately work on.  Have a fuzzy idea?  Want some feedback or help brainstorming a project?  **Come to office hours and/or recitation.  The staff are all here to help!**


<a name="proposal" />
### Proposal

Your research proposal will contain an overview of the research problem, _your hypothesis_, first pass at related work, a description of how you plan to complete the project, and metrics to decide _if it worked_.   


We have setup a template for your proposal on overleaf.  Clone it into your team's account to edit it.  Make sure to change the title and author names, and include your team members' UNIs.


**Submission**

1. Use the [proposal template on Overleaf](https://www.overleaf.com/read/xhpgqyqbghry)
1. [Click here to submit](#)




<a name="draft" />
### Paper Draft

You will submit a draft of your paper that should be between 4 -- 6 pages. Please use the [overleaf report template](https://www.overleaf.com/read/phmrptrtjrhz) to get started.  It already contains a scaffold of sections, and suggestions of what to include in each section.  Your report is not beholden to these sections, so take the template as a starting point.  

For the draft, you should have a fleshed out introduction, related work, and technical overview.  You should have a clearer idea of the technical details than from the proposal, but need not have implemented it yet.  You do not need to have run experiments yet, but should sketch out the hypotheses and the potential experiment setup (which may change). If you have preliminary findings, that's great!  Please include those.

In short, I expect that you have a much clearer idea about the problem _and_ how it can be solved.  Most of the technical details and relevant work should be clear, but you may not have implemented it yet.


Tips:

* [Tips for Writing Technical Papers - Jennifer Widom, Dean of Stanford Engineer](https://cs.stanford.edu/people/widom/paper-writing.html)

**Submission**

1. Use the [report template on Overleaf](https://www.overleaf.com/read/phmrptrtjrhz)
1. [Click here to submit](#)



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

<a name="suggestions"></a>
## Project Suggestions


TBA

<!--
The following are examples of possible projects -- they are by no means a complete list and **you are free to select your own projects**.  In fact, a common source of ideas is to take your experience from another domain, and combine it with databases/data management.  Projects often come in several flavors:

0. Make DataBass better: extend DataBass in a significant way, and evaluate it against other systems.  For instance, support DSM/PAX, Apache Arrow, distributed execution, LLVM compilation, lineage, etc.  Code quality matters for this option.
1. Research project: model an unsolved problem, propose algorithmic solution, evaluate and report findings.
2. Win: pick an existing useful application and a well-recognized metric (latency, prediction, etc) and win against the state of the art.
3. Break and fix: implement a state of the art algorithm on real data, show that it doesn't actually work (results are poor, it's slow, etc), make it work.
4. Evaluate: there are many options out there, it's not clear which ones are actually best, and under what conditions.  Run a bake-off and evaluate.
5. Fill a gap:  think about something useful that _should_ be easily doable, but is painful or impossible with current state of the art.  Fill that gap.
-->





<!--

khameleon

* serverless/lmfao -> scalable backend
* progressively encoded and computed data cubes

databass/pysmoke

* apps of lineage
  * visualize lineage by leveraging the charts and queries 
    used to generate the lineage
  * smoke hilda
* add WCO joins and explore vicktor's paper
* databass -> rust / js
* columnar
* incorporate something interesting fro the readings
  * why not summarization
* use databass to do incremental computation in an incremental fashion (dbtoaster)
  * bonus: incremntally maintain lineage indexes
* benchmark vega and diff dataflow, find benchmarks
* add an IR, define the IR
* adding different access methods and extend optimizer to recognize

evaluate ml in databases

smoke for pandas?

* hand instrument c code for some operators to show feasibility

* expand on diffparsing with query language, apply to non-sql programs

cross layer signals for ML in systems

* informative features come from
  * interface feoatures from a viz that generate queries that run on the index
  * ast/query plan features that are known before the query is executed
  * batches of data that are inserted into the index
* find a learned index, show that adding occassional informative features 
  improves the model accuracy
* show that adding a mixture of informative and uninformative features 
* show that it improves the actual index performance on serial workloads
* what happens on a mixture of concurrent workloads
* connect to logging infrastructure

combining a streaming system with realitysketch ideas

rain

IFC for concurrency control

-->


<!--

Potential ideas

* Apache Arrow is the defacto standard for moving data around.  Build an in-browser fast execution engine for apache arrow using asm and typed arrays.  You can assume that only foreign key joins are used (cardinality will not explode).
* query compiler to rust
* RL across execution layers 
* Some RL + data structure business


* Visualizations and clients currently need to poll from materialized
  * the system supports creating streaming sinks
  * extend vega lite to rewrite subsets of the spec into
    materialized views that can stream changes directly to the client.

use lineage in interesting ways

* not "show inputs", not "whynot"
* actually use it -- implement smoke hilda


-->
