---
layout: post
title: Smart Reply - Overview of the paper
comments: true
---

When you use Google <a href="https://allo.google.com/">Allo</a> or <a href="https://www.blog.google/products/gmail/computer-respond-to-this-email/">GMail</a> on your mobile device, you have to see suggestion which the app provides when you receive a short message.

In, <a href="http://www.kdd.org/kdd2016/papers/files/Paper_1069.pdf">the cover paper - Smart Reply: Automated Response Suggestion for Email</a>, we can observe several interesting ideas. I will write some of then in a short list below. If you want to read it all by yourself, I will strongly encourage you to do it, but at the end of this post is also a highligted version.

  * The system is already in the production with responsibily for more than 10% replies on mobile phone. (with keeping in the mind that the trigger mechanism keep a majority of messages without a suggestion)
  * About 25% of replies has even or less than 20 tokens (words)
  * LSTM can be used generate unique reply to every input message, BUT then there will be problem with 
    * Response quality
    * Likehood that reply will be chosen
    * Scalability
    * Privacy - can show names or other stuff because they will be in the vocabulary
  * LSTM is used in smarter way and just select responses from pregenerated sets (good grammar)
  * To make a base set of resposnes is used semi-supervised algorithm (+ Expander)
  * All response messages should be part of the "semantic" cluster - from these clusters are chosen response
  * What about redundant/duplicite responses - delete them 
  * What if all sugested responses are positive/negative - delete majority and enforce minority
  * Dealing with text = preprocces it -> tokenize sentences -> tokenize words -> remove names/number etc.
  * Dealing with email = preprocces it -> a quoation/signature/salutation removal

A PDF document with highlighted interesting parts is <a href="{{ site.baseurl }}/files/pdf/Smart Reply- Automated Response Suggestion for Email.pdf" >here</a>.




















