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
* Report        12-15   (40%)



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
1. [Click here to submit your **4 -- 6 page** draft](https://easychair.org/conferences/?conf=w611320)
  * Please see [this draft from a previous class](https://www.dropbox.com/s/y460nkyi7pmnkre/example%20draft.pdf?dl=0) as an example.



### <a name="showcase"/>Project Showcase 

Your team will prepare and present a project poster at the end-of-course showcase session.   This gives you an opportunity to present a short presentation demo of your work and show what you have accomplished in the class!  

Your presentation should be polished.  Since there is still time until the final report, you are encouraged to also discuss ideas or challenges you are still considering.  

**Since you are presenting to your peers as well, make sure you give your colleagues enough context to understand your ideas.  In addition to _what_ you did, help your colleagues understand _why_ you made your specific choices, and provide examples.  It's better to make sure the audience learns a few specific ideas than try to say everything.**  Come to office hours or contact the staff if you would like feedback.

Overall logistics

* team will be given 10 minutes : 5 min presentation, 5 min q&a and feedbacks
* Timing is strict since we have many groups.  *Practice ahead of time so your presentation is smooth!  Only takes 5 minutes per practice :)*
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

* Submit URL to your group's [PDF file or google slides](https://forms.gle/Ck1FX3higgbVUHkA9)
* Deadline for submission: Tuesday, 12/08/2020 11:59 PM


### Report/Camera Ready

You will revise your draft and submit a conference-style report on your project, with **maximum length** of 12 pages. 
Because this report is the primary deliverable upon which you will be graded, **do not treat it as an afterthought**. Plan to leave at least a week to do the writing, and make sure your proofread and edit carefully!

**Submission**

* Deadline: Tuesday, December 15 2020
* [Submit here.  Name your file UNI_UNI.pdf](https://www.dropbox.com/request/HzQwTw6CpdST28wMvyFS) 


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
