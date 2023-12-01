#!/usr/bin/env python
# coding: utf-8

# In[28]:


with open("day3.txt") as f:
	total = 0
	for l1,l2,l3 in zip(*([map(str.strip, f)]*3)):
		(c,) = set(l1) & set(l2) & set(l3)
		prio = ord(c) - ord('a') if ord(c) >= ord('a') else ord(c) - ord('A') + 26
		total += prio + 1
total

