#!/usr/bin/env python
# coding: utf-8

# In[81]:


import itertools

def next_coord(move, cur):
	if move == "R": return (cur[0]+1, cur[1])
	if move == "U": return (cur[0], cur[1]+1)
	if move == "L": return (cur[0]-1, cur[1])
	if move == "D": return (cur[0], cur[1]-1)

def follow_coord(prevknot, cur):
	normalize = lambda v: v // abs(v) if v != 0 else 0
	mx, my = map(normalize, [prevknot[0] - cur[0], prevknot[1] - cur[1]])
	return cur[0] + mx, cur[1] + my

with open("day9.txt") as f:
	knots = [(0, 0)]*2 # number of knots
	visited = { knots[-1] }
	
	moves = itertools.chain(*(m*int(c) for m, c in map(str.split, map(str.strip, f))))
	for move in moves:
		is_close = lambda k1, k2: abs(k1[0] - k2[0]) <= 1 and abs(k1[1] - k2[1]) <= 1
		follow = lambda k1, k2: k2 if is_close(k1, k2) else follow_coord(k1, k2)
		knots = list(itertools.accumulate(knots[1:], func=follow, initial=next_coord(move, knots[0])))
		
		visited.add(knots[-1])

len(visited)

