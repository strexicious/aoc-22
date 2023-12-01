#!/usr/bin/env python
# coding: utf-8

# In[37]:


G = { }
rates = { }
with open("day16.txt") as f:
	for l in map(str.split, map(str.strip, f)):
		v = l[1]
		exec(l[4])
		ev = [e.replace(",","") for e in l[9:]]
		G[v] = ev
		rates[v] = rate
N = len(G)
v2i = { v: i for i, v in enumerate(G) }
i2v = { i: v for v, i in v2i.items() }


# In[38]:


import numpy as np

Gw = np.ones((N, N), dtype=int)*int(1e6)
for v, ev in G.items():
	Gw[v2i[v], v2i[v]] = 0
	for nv in ev:
		Gw[v2i[v], v2i[nv]] = 1
		Gw[v2i[nv], v2i[v]] = 1


# In[39]:


for i in range(N):
	for j in range(N):
		for ni in range(N):
			if Gw[i, j] > Gw[i, ni] + Gw[ni, j]:
				Gw[i, j] = Gw[i, ni] + Gw[ni, j]
				Gw[j, i] = Gw[i, ni] + Gw[ni, j]


# In[44]:


# takes about 38s on my machine and python setup

import itertools
import functools

# 1) from the given input sparse graph we generate a fully connected
# dense weighted graph `Gw`, where each edge weight is min-path
# length in the original sparse graph between the corresponding vertices
# 2) the `v2i` and `i2v` are helper mappings between two-letter vertex tags
# and assigned integer
# 3) rates for each vertex/valve are stored in the `rate` mapping

# before I was trying to use a bottom-up tabulating dynamic programming
# but even before that I had this function written
# I had thought that the state space for subproblems was (v, mins_left) but
# I was using visited set as well in the paremeter. After having it confirmed on
# reddit that all three parameters define state space, I just slapped @cache

@functools.cache
def visit(v, visited, mins_left):
	if rates[v] == 0: return 0, tuple() # short circuit, idea from reddit
	if mins_left < 2: return 0, tuple()
	if N == len(visited): return 0, tuple()
	
	best = rates[v] * (mins_left - 1)
	nxt = tuple()
	for ni, w in enumerate(Gw[v2i[v]]):
		nv = i2v[ni]
		
		if nv == v: continue
		if nv in visited: continue
		
		r, nxts = visit(nv, visited + (v,), mins_left - w - 1)
		
		if rates[v] * (mins_left - 1) + r > best:
			best = rates[v] * (mins_left - 1) + r
			nxt = nxts

	return best, (v, *nxt)

tuple(visit(i2v[ni], ("AA",), 26 - w) for ni, w in enumerate(Gw[v2i["AA"]]))


# In[ ]:


used = [[{ v } for v in range(N)] for _ in range(31)]
nxts = [[-1]*N for _ in range(31)]
bests = np.zeros((31, N), dtype=int)

for mins in range(2, 31):
	for v in range(N):
		best = rates[i2v[v]] * (mins - 1)
		nxt = None
		for ni, w in enumerate(Gw[v]):
			if mins-w-1 < 2: continue
			if v in used[mins-w-1][ni]: continue
			if rates[i2v[v]] * (mins - 1) + bests[mins - w - 1, ni] > best:
				best = rates[i2v[v]] * (mins - 1) + bests[mins - w - 1, ni]
				nxt = ni
		bests[mins][v] = best
		if nxt != None:
			used[mins][v] = used[mins-Gw[v,nxt]-1][nxt] | { v }
			nxts[mins][v] = nxt
		else:
			used[mins][v] = { v }

# min_left = 30
# acc = 0
# cv = v2i["AA"]
# used = { v: False for v in G }

# while min_left > 0:
# 	print(min_left, acc, best, i2v[cv])
# 	nxt = None
# 	best = 0
# 	for ni, w in enumerate(Gw[cv]):
# 		if used[i2v[ni]]: continue
# 		if min_left - w >= 1 and rates[i2v[ni]] * (min_left - w - 1) > best:
# 			nxt = ni
# 			best = rates[i2v[ni]] * (min_left - w - 1)
# 	if nxt == None:
# 		break
# 	min_left = min_left - Gw[cv, nxt] - 1
# 	cv = nxt
# 	acc += best
# 	used[i2v[nxt]] = True


# In[ ]:


np.asarray(nxts), np.asarray(bests), Gw

