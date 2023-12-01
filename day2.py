#!/usr/bin/env python
# coding: utf-8

# In[17]:


l2i = str.maketrans("ABCXYZ", "012036")
with open("day2.txt") as f:
	score = 0
	for l in f:
		o, m = map(int, l.strip().translate(l2i).split())
		score += m
		move = m // 3 - 1
		score += (o + move) % 3 + 1
score

