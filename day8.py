#!/usr/bin/env python
# coding: utf-8

# In[168]:


import numpy as np

SIZE = 99
grid = np.zeros((SIZE, SIZE), dtype=np.int8)
vis_map = np.zeros((SIZE, SIZE), dtype=bool)

with open("day8.txt") as f:
	for i, l in enumerate(map(list, map(str.strip, f))):
		grid[i] = np.fromiter(map(int, l), dtype=grid.dtype)

# tovisit = [(0, i) for i in range(0, SIZE)] + [(i, -1) for i in range(1, SIZE)] + [(-1, i) for i in range(SIZE-2, -1, -1)] + [(i, 0) for i in range(SIZE-2, 0, -1)]
# vis_map[tuple(zip(*tovisit))] = True

maxes = np.zeros((SIZE,), dtype=np.int8) - 1
for i, r in enumerate(grid.T):
	vis_map.T[i] |= r > maxes
	maxes = np.max([maxes, r], axis=0)

maxes = np.zeros((SIZE,), dtype=np.int8) - 1
for i, r in enumerate(grid):
	vis_map[i] |= r > maxes
	maxes = np.max([maxes, r], axis=0)

maxes = np.zeros((SIZE,), dtype=np.int8) - 1
for i, r in enumerate(grid.T[::-1]):
	vis_map.T[SIZE-1-i] |= r > maxes
	maxes = np.max([maxes, r], axis=0)

maxes = np.zeros((SIZE,), dtype=np.int8) - 1
for i, r in enumerate(grid[::-1]):
	vis_map[SIZE-1-i] |= r > maxes
	maxes = np.max([maxes, r], axis=0)

np.sum(vis_map)

# visible = np.zeros((SIZE,SIZE), dtype=bool)
# visible[:,0] = True
# visible[0,:] = True
# visible[:,-1] = True
# visible[-1,:] = True
# print(visible[tuple(zip(*tovisit))])



# In[169]:


import itertools
max_score = 0
for i, j in itertools.product(range(SIZE), range(SIZE)):
	score = 1
	vdist = 0
	for k in range(i+1, SIZE):
		vdist += 1
		if grid[k, j] >= grid[i, j]: break
	score *= vdist
	
	vdist = 0
	for k in range(j+1, SIZE):
		vdist += 1
		if grid[i, k] >= grid[i, j]: break
	score *= vdist
	
	vdist = 0
	for k in range(i-1, -1, -1):
		vdist += 1
		if grid[k, j] >= grid[i, j]: break
	score *= vdist
	
	vdist = 0
	for k in range(j-1, -1, -1):
		vdist += 1
		if grid[i, k] >= grid[i, j]: break
	score *= vdist

	max_score = max(score, max_score)
max_score

