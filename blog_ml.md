---
layout: page
author: Petr Lorenc
permalink: /blog_ml/
---

<div class="posts">
  {% for post in site.postsml %}
    {% if post.tag == "machine learning" %}
      <article class="post">

        <h1><a class="title" href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>

        <div class="date">
  	    Written on {{ post.date | date: "%B %e, %Y" }}
  	  </div>

        <div class="entry">
          {{ post.excerpt }}
        </div>
        
        <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
      </article>
    {% endif %}
  {% endfor %}
</div>