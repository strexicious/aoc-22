#!/usr/bin/env python
# coding: utf-8

# In[38]:


from functools import cmp_to_key

import itertools

def compare(a, b):
	for ea, eb in zip(a, b):
		if isinstance(ea, int) and isinstance(eb, int):
			if ea < eb: return 1
			if ea > eb: return -1
			continue

		if isinstance(eb, int):
			eb = [eb]

		if isinstance(ea, int):
			ea = [ea]
		
		sublist = compare(ea, eb)
		if sublist in [-1, 1]:
			return sublist
	
	return 1 if len(a) < len(b) else -1 if len(a) > len(b) else 0

with open("day13.txt") as f:
	it = map(eval, filter(str, map(str.strip, f)))
	# idx_sum = 0
	# for i, (a, b) in itertools.islice(enumerate(zip(it, it), start=1), None):
	# 	if compare(a, b) == 1:
	# 		idx_sum += i
	
	ordered = list(sorted(itertools.chain(it, [[[2]], [[6]]]), key=cmp_to_key(compare), reverse=True))
	print(ordered.index([[2]]) + 1, ordered.index([[6]]) + 1)


# In[39]:


124*208

