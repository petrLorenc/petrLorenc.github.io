---
layout: post
title: Natural Language Processing Part 1 
tag: machine learning
---

My current research is about NLP with Czech text - I would like to use this interesting topic to be my diploma thesis, so I also decided to create this series to make accessible this interesting topic to everyone. In this series of post I would like to show some pitfalls which I have to encounter with. I will try to make as general as possible (it means that I won't be focused on Czech text but on text in general).

Firstly, we need to mention what kind of problems are typically solved in NLP. The basic and most general is the machine translation, it is almost the Holy Grail to create Babel fish. But there also other no-less important fields. I would like to mention chat-bots, email clustering, spam detection and much more.

But almost all research in the text has something in common - preprocessing and text representation. 

For preprocessing we usually talk about stop-word removal (words that has no importance - sometimes is hard to define what is important and what is not), <a href="https://en.wikipedia.org/wiki/Stemming">stemming</a> (remove prefix and suffix) and <a href="https://en.wikipedia.org/wiki/Lemmatisation">lemmatization</a> (transfer the word to his base form).

For the text representation is often used <a href="https://en.wikipedia.org/wiki/Bag-of-words_model">BOW</a> (Bag Of Words), which has several drawbacks - there is very sparsity of data and there are no semantic in the text representation - we can have words with similar meaning but in BOW model they would be as far as every other word. This problem is partially solved by the <a href="https://en.wikipedia.org/wiki/Word_embedding">word embedding</a>. There will be a separate post about them (they have a very interesting process of constructing them and they preserve semantic).

Lastly, I would like to mention <a href="https://en.wikipedia.org/wiki/N-gram">n-grams</a> (it depends on the order of words - in opposite of co-occurrence, where we focus only on the occurrence of words), which can used to create very basic and easy text generator.

{% highlight python %}

import nltk
import random
from nltk.util import ngrams

text = None
with open('speech.txt', 'r') as f:
	text = f.read()
ng = ngrams(nltk.word_tokenize(text),2) # we use bi-grams
fd = nltk.ConditionalFreqDist(ng)

word = "the" # seed
output = [] # output list of words
for i in range(15):
	output.append(word)
	word = random.choice(list(fd[word].keys()))
print(" ".join(output))

{% endhighlight %}

You can look at the code in <a href="https://github.com/petrLorenc/tutorials/blob/master/NLP/Generate_text_ngram.ipynb">github</a>.

