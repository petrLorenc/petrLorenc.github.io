---
layout: page
author: Petr Lorenc
permalink: /blog/
---

<div class="posts">
  {% assign all_posts = site.posts | where_exp: "post", "post.category != 'machine_learning'" %}
  {% for post in all_posts %}
    <article class="post">

      <h1><a class="title" href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>

      <div class="date">
        Written on {{ post.date | date: "%B %e, %Y" }}
        {% if post.category %}
          | Category: <a href="{{ site.baseurl }}/{{ post.category }}/">{{ post.category | replace: '_', ' ' | capitalize }}</a>
        {% endif %}
      </div>

      <div class="entry">
        {{ post.excerpt }}
      </div>
      
      <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
    </article>
  {% endfor %}
</div>