#!/usr/bin/env python
# coding: utf-8

# In[13]:


import itertools
all_different = lambda c: sum(int(p[0] == p[1]) for p in itertools.product(c, c)) == 14
with open("day6.txt") as f:
	for l in f:
		chars_window_iter = zip(*(iter(l[i:]) for i in range(14)))
		for i, chars in enumerate(chars_window_iter):
			if all_different(chars):
				print(i+14)
				break

