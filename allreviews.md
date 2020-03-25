---
layout: page
---
<style>
p.review {
  border-left: 2px solid grey;
}

div.block {
  margin-bottom: 1em;
}
</style>


{% assign reviews3 = site.data.reviews3 | reverse %}
{% assign reviewsall = site.data.reviewsall %}

## Short Summaries

{% for r in reviews3 %}
  <h3>{{r.Timestamp}} {{r.Name}}</h3>
  <p class="block">{{ r.Contribution | newline_to_br | safe }}</p>
{% endfor %}


## Reviews
{% for r in reviews3 %}
  <p class="review">
  <h3>{{r.Timestamp}} {{r.Name}}</h3>

  <div>Response:</div>
  <p class="block">{{ r.Review | newline_to_br | safe }}</p>
  <div>Comments:</div>
  <p class="block">{{ r.Comments | newline_to_br | safe }}</p>
  <div>Predictions 1:</div>
  <p class="block">{{ r.Prediction1 | newline_to_br | safe }}</p>
  <div>Predictions 2:</div>
  <p class="block">{{ r.Prediction2 | newline_to_br | safe }}</p>
   <div>Predictions 3:</div>
  <p class="block">{{ r.Prediction3 | newline_to_br | safe }}</p>
  
  </p>
  <hr/>
{% endfor %}




