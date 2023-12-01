#!/usr/bin/env python
# coding: utf-8

# In[32]:


from collections import defaultdict
from os import path

cur_estimate = 1e10
def sizeup(dirs, d, depth=0):
	global cur_estimate
	size = sum(item[1] if len(item) == 2 else sizeup(dirs, item[0], depth+1) for item in dirs[d])
	if 2476859 <= size < cur_estimate:
		cur_estimate = size
	return size

with open("day7.txt", "r") as f:
	dirs = defaultdict(set)
	cur_path: str = "/"
	for l in map(str.split, map(str.strip, f)):
		if l[:2] == ["$", "cd"]: cur_path = path.normpath(path.join(cur_path, l[2]))
		elif l[:2] == ["$", "ls"]: pass
		elif l[0] == "dir": dirs[cur_path].add((path.normpath(path.join(cur_path, l[1])),))
		else: dirs[cur_path].add((l[1], int(l[0])))

sizeup(dirs, "\\")
cur_estimate


# In[30]:


30000000-27523141

