#!/usr/bin/env python
# coding: utf-8

# In[12]:


with open("day4.txt") as f:
	total = 0
	for l in f:
		r1, r2 = l.strip().split(",")
		torange = lambda r: list(map(int, r.split("-")))
		inother = lambda r1, r2: r1[0] <= r2[0] <= r1[1] or r2[0] <= r1[0] <= r2[1]
		total += int(inother(torange(r1), torange(r2)))
total

