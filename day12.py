#!/usr/bin/env python
# coding: utf-8

# In[105]:


from dataclasses import dataclass

import itertools

grid = []

with open("day12.txt") as f:
	for i, l in enumerate(f):
		if (Si := l.find("S")) != -1: start = (i, Si)
		if (Ei := l.find("E")) != -1: end = (i, Ei)

		replaceSE = lambda c: "a" if c == "S" else "z" if c == "E" else c
		grid.append([-ord(replaceSE(c)) + ord('a') for c in l.strip()])

W = len(grid[0])-1
H = len(grid)-1
tovisit = { coord: 1e10 for coord in itertools.product(range(H+1), range(W+1))}
tovisit[end] = 0
while tovisit:
	ny, nx = min(tovisit, key=tovisit.__getitem__)
	step = tovisit[ny, nx]

	if grid[ny][nx] == 0: # or (ny, nx) == start
		print(step)
		break
	
	if nx > 0 and grid[ny][nx-1] - grid[ny][nx] < 2 and tovisit.get((ny, nx-1), -1) > step:
		tovisit[ny, nx-1] = step+1
	if ny > 0 and grid[ny-1][nx] - grid[ny][nx] < 2 and tovisit.get((ny-1, nx), -1) > step:
		tovisit[ny-1, nx] = step+1
	if nx < W and grid[ny][nx+1] - grid[ny][nx] < 2 and tovisit.get((ny, nx+1), -1) > step:
		tovisit[ny, nx+1] = step+1
	if ny < H and grid[ny+1][nx] - grid[ny][nx] < 2 and tovisit.get((ny+1, nx), -1) > step:
		tovisit[ny+1, nx] = step+1
	
	del tovisit[ny, nx]


# In[95]:


from matplotlib import pyplot as plt

import numpy as np

img = np.zeros((W+1, H+1), dtype=np.uint8)
indices = list(zip(*(coord for coord in itertools.product(range(H+1), range(W+1)) if coord not in tovisit)))
img[indices[1], indices[0]] = 64
img[start] = 180
img[end] = 255
plt.imshow(img)
plt.show()


# In[60]:


pathmap = [["."]*len(grid[0]) for _ in range(len(grid))]

go = path[end]
while go != start[:2]:
	print(go)
	go = path[go]

