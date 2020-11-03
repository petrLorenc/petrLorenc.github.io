---
layout: post
title: Generative and discriminative models (ENG)
description: First attempt to summarize very broad topic of generative and discriminative models. I will be glad for every suggestion or discussion over this topic. I am sorry for math formulas but I wasn't able to make it work yet.
author: Petr Lorenc
comments: true
---

First attempt to summarize very broad topic of generative and discriminative models. I will be glad for every suggestion or discussion over this topic.
I am sorry for math formulas but I wasn't able to make it fully work yet. I will be trying to improve it over time.

# Generative models:
  * Estimates the joint probability distribution of data **P(X, Y)** between the observed data X and corresponding labels Y
  * Provides a way to sample X, Y pairs
  * To impute missing data, compress your dataset or generate unseen data.

\\[ argmax_yP(Y=y|X=x)= argmax_y(\frac{P(Y=y,X=x)}{P(X=x)}) \\] since P(X=x) is constant in argmax over y function so: 
\\[ argmax_yP(Y=y,X=x)  \\]



# Conditional Independence:
  * If we can say that P(X|Y,Z) = P(X|Z) then X is conditionally independent of Y given Z

\\[ P(X|Y) = P(X1,X2|Y)  \\] 
= general property of probabilities 
= \\[  P(X1|X2,Y)P(X2|Y)  \\] 
= conditional independence assumption  
= \\[  P(X1|Y)P(X2|Y) \\]

# Method to estimate parameters:
  * MLE is a special case of MAP, where the prior is uniform
  * MLE - param = 
\\[  argmax_p P(data|p) = argmax_p SUM(log(P(data|p)))  \\]
  * MAP - param = 
\\[  argmax_p P(data|p)\*P(p)  = argmax_p SUM(log(P(data|p)\*P(p))) \\]
  * <a href="https://wiseodd.github.io/techblog/2017/01/01/mle-vs-map/">MLE vs MAP</a>

# Naive Bayes
  * Generative model (joint probability **P(Y,X)**)
  	* The basic idea is, first, to establish the probability density model of the sample, and then use the model for inference prediction
  	* I have to care about a distribution of the Y and also the X
  * Need to assume that features are independent
     * P(spam\|"win" and "buy") = P(spam|win) * P(spam|buy)
  * Train time: O(log n)
  	* Discrete variant
	    * Maximum likehood estimates - count occurences (can be smoothed - Laplace smoothing)
	    * Maximum a posteriori estimation - if we assume a Dirichlet prior distribution then it is like Laplace smoothing
	* Continuos
		* Usually assuming Gaussian distribution of features
		* Estimating Mean and Standart deviation
		* <a href="http://www.cs.cmu.edu/~tom/mlbook/NBayesLogReg.pdf">Section 2.4.</a> 

# Discriminative models:
  * P(tags\|data)

# Logistic regression
  * Dicriminitive model (conditional probability **P(Y|X)**)
    * The basic idea is to establish the discriminant function with finite samples, and directly study the prediction model without considering the generative model of samples.
    * To don't need a distribution of X
  * Sigmoid function on the output of the model -> treshold determine 0/1 (in binomial case)
    * Can be shown that the decision boundary is: Assign "Y=0" given "data" if 0 < w_0 + SUM(w_i* X_i) 
    * <a href="http://www.cs.cmu.edu/~tom/mlbook/NBayesLogReg.pdf">Section 3</a>
  * Try to find a relationship between output and input (via features)
  * Train time: O(n)
    * Gradient descent with respect to param vector W (with regularization)
  * Need generally more data than Naive Bayes
  * **Naive Bayes can be derived from Logistic expression <a href="http://www.cs.cmu.edu/~tom/mlbook/NBayesLogReg.pdf">Section 3.1</a>**

<figure class="image" align="middle">
  <a href="{{ site.baseurl }}/images/classifiers/arrow.png" data-lightbox="Determine words from tag" data-title="Determine words from tag" data-lightbox="roadtrip">
    <img src="{{ site.baseurl }}/images/classifiers/arrow.png" alt="Determine words from tag" title="Determine words from tag"/>
    <figcaption>Determine words from tag</figcaption>
  </a>
</figure>

<figure class="image" align="middle">
  <a href="{{ site.baseurl }}/images/classifiers/reverse_arrow.png" data-lightbox="Determine tag from words" data-title="Determine tag from words" data-lightbox="roadtrip">
    <img src="{{ site.baseurl }}/images/classifiers/reverse_arrow.png" alt="Determine tag from words" title="Determine tag from words"/>
    <figcaption>Determine tag from words</figcaption>
  </a>
</figure>

# HMM
  * Generative model (joint probability **P(states,data)**)
    * Any observation sequence may be generated.
    * Also concern distribution over data
  * Get prediction with Viterbi algorithm
  * Create directed graph
  * **Each state s_i depends only on state s_i-1 (Markov property)**
  * Each observation o_i depends only on current state s_i
  * Propability distribution: 
    * **Initial**  - Probability of a state at the beginning
    * **Transition** - Probability of a transition from state A to state B
    * **Observation** - Probability of emision a visible output from state
  * Easier to estimate than CRF
  * Assume conditionally independence over data (X_i does't corelate with X_i+1)

<figure class="image" align="middle">
  <a href="{{ site.baseurl }}/images/classifiers/HMM.png" data-lightbox="Hidden Markov Model" data-title="Hidden Markov Model" data-lightbox="roadtrip">
    <img src="{{ site.baseurl }}/images/classifiers/HMM.png" alt="Hidden Markov Model" title="Hidden Markov Model"/>
    <figcaption>Hidden Markov Model</figcaption>
  </a>
</figure>

# CRF
  * Dicriminitive model (conditional probability **P(states\|data)**)
    * No assumptions about P(data)
  * Versions:
    * **linear CRF** (only previous item in input sequence - similar to Markov assumption)
    * **general CRF** (you can use each item in input sequence)
  * Need to manually specify feature/potential function
    * can be indicator of some feature (fire up when some feature occur) - assign weights
  * Get prediction with Viterbi algorithm
  * Create undirected graph
  * Basic principle is multiplication of feature functions with learning weights
  * **Logistic regression is very simply CRF (only one feature function)**

<figure class="image" align="middle">
  <a href="{{ site.baseurl }}/images/classifiers/CRF.png" data-lightbox="Conditional Random Field" data-title="Conditional Random Field" data-lightbox="roadtrip">
    <img src="{{ site.baseurl }}/images/classifiers/CRF.png" alt="Conditional Random Field" title="Conditional Random Field"/>
    <figcaption>Conditional Random Field</figcaption>
  </a>
</figure>

<figure class="image" align="middle">
  <a href="{{ site.baseurl }}/images/classifiers/all.png" data-lightbox="All three models" data-title="All three models" data-lightbox="roadtrip">
    <img src="{{ site.baseurl }}/images/classifiers/all.png" alt="All three models" title="All three models"/>
    <figcaption>All three models</figcaption>
  </a>
</figure>

# Resources:
  * <a href="https://liqiangguo.files.wordpress.com/2011/04/hmm-memm-crf.pdf">HMM vs MEMM vs CRF</a>
  * <a href="http://www.cs.cmu.edu/~tom/mlbook/NBayesLogReg.pdf">Naive Bayes and Logistic Regression</a>
  * <a href="https://wiseodd.github.io/techblog/2017/01/01/mle-vs-map/">MLE vs MAP</a>