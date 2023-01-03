---
layout: index
---


#### Overview

Data management systems are the corner-stone of modern applications, businesses, and science (including data).  If you were excited by the topics in 4111,  this graduate level course in database systems research will be a deep dive into classic and modern database systems research.  Topics will range from classic database system design, modern optimizations in single-machine and multi-machine settings, data cleaning and quality, and application-oriented databases.

The class places a heavy emphasis on paper reading and writing good paper reviews. The point is to practice reading papers critically, writing proper reviews, implementing ideas in research papers, and conducting research. As such, students will be expected to read papers in depth, complete assignments based ideas from the readings, and conduct a semester-long research project.

Ideally, you will be comfortable with reading code that is not yours, open to trying different software systems, and willing to actively participate in and lead discussions.

See [FAQ](./syllabus#faq) for difference between 6113 and the other database courses. 

<small style="color: grey">Course capped at 25. </small>



#### Recent Announcements


#### Tentative Schedule


<style>
.presenter { }
</style>

<table class="table table-striped schedule">
  <thead>
  <tr>
    <!--<th class="idx" style="width: 3em; max-width:3em;"></th>-->
    <th class="date" style="width: 15em; max-width: 15em;"> <p> <span>Date </span> </p> </th>
    <th style="min-width: 15%;"> <p> <span>Topic </span> </p> </th>
    <th style="width: 10%"> <p> <span>Notes </span> </p> </th>
    <th style="width: 15%;"> <p> <span>Assigned</span> </p> </th>
    <th style="width: 15%;"> <p> <span>Due</span> </p> </th>
  </tr>
  </thead>
{% assign idx = 0 %}

{% for r in site.data.schedule %}
  {% assign idx = idx | plus: 1  %}
  <tr style="background-color: {{r.color}}; ">
    <!--<td class="idx">C{{idx}}</td>-->
    <td class="date">C{{idx}}: {{r.date}}</td>
    <td class="slug">
      {% if r.link %}
        <a href="./papers#{{r.link}}"><b>{{r.slug}}</b></a>
      {% else %}
        <b>{{r.slug}}</b>
      {% endif %}
      {% if r.presenter %}
        <br/>
        <span class='presenter'>Presenter: {{r.presenter}}</span>
      {% endif %}
      {% if r.notes %}
        <br/>
        {{r.notes|raw}}
      {% endif %}
      </td>
    <td class="notes">
    </td>
    <td>{{r.assigned | safe}}</td>
    <td>{{r.due | safe}}</td>
  </tr>
{% endfor %}
</table>


