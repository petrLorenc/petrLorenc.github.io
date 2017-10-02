---
layout: post
title: Improving deep neural networks: hyperparameter  - deeplearning.ai
comments: true
---

I just started Improving deep neural networks course (second part) created by deeplearning.ai on the <a href="https://www.coursera.org/learn/neural-networks-deep-learning/home/welcome">Coursera</a>. I would like to write here my progress and use this place as a notebook.

- Train/Dev/Test

	- If you have a lot of data you should divide your dataset into Train/Dev/Test in ration about 98/1/1% because if you have for example 1 000 000 data points then 1% (10 000) is enough for Dev/Test where you want to just pick a right model.
	- Watch for correct data in whole dataset. They should come from the same distribution. (Pictures from website VS. Pictures from mobile camera)

High bias usually means underfitting, in the oppossite high variance means overfitting. We can get a clue from train/dev set error. We should determine what is the human error limit (say that human are perfect in some task so the limit will be almost 0%). If we have small error on train (1%) and bigger on dev (11%) then we are dealing with high variance, but if we have big error on train (around 15%) and almost the same on dev (around 16%) we are heading to high bias. It can have both (high bias and high variance)








