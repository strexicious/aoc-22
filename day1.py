#!/usr/bin/env python
# coding: utf-8

# In[43]:


import itertools
sum(sorted(map(lambda g: sum(map(int, g[1])), filter(lambda g: g[0], itertools.groupby(map(str.strip, open("day1.txt")), bool))))[-3:])

