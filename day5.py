#!/usr/bin/env python
# coding: utf-8

# In[7]:


import itertools

with open("day5.txt") as f:
	stack_inp = list(itertools.takewhile(str.strip, f))
	stacks = [[] for i in range(len(stack_inp[-1])//4)]
	
	for l in stack_inp[-2::-1]:
		non_space = lambda el: not el[1].isspace()
		bottom_up_stacks_iter = filter(non_space, enumerate(l[1::4]))
		for i, e in bottom_up_stacks_iter:
			stacks[i].append(e)

	for l in f:
		_, els, _, f, _, t = l.split()
		els, f, t = map(int, [els, f, t])
		stacks[t-1] += stacks[f-1][-els:]
		stacks[f-1][-els:] = []
		# for _ in range(els):
		# 	stacks[t-1].append(stacks[f-1].pop())

print("".join(s[-1] for s in stacks if s))
			

