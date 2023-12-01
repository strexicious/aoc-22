#!/usr/bin/env python
# coding: utf-8

# In[165]:


from collections import Counter
from functools import reduce

import itertools
import operator

def cleaned_monkey(desc):
	items = [int(i.replace(",", "")) for i in desc[1][2:]]
	op = desc[2][-3:]
	op = " ".join(desc[2][-3:])
	return desc[0][1][:-1], items, op, int(desc[3][-1]), desc[4][-1], desc[5][-1]

monkey_items = {}
monkey_ops = {}
monkey_tests = {}
with open("day11.txt") as f:
	for monkey in zip(*[map(str.split, map(str.strip, f))]*7):
		mid, items, operation, test, pf, nf = cleaned_monkey(monkey)
		monkey_items[mid] = items
		monkey_ops[mid] = operation
		monkey_tests[mid] = (test, pf, nf)
BIGN = reduce(operator.mul, (t[0] for t in monkey_tests.values()))


# In[156]:


monkey_counts = Counter()
for _ in range(20):
	for mid, items in monkey_items.items():
		monkey_counts[mid] += len(items)
		for item in items:
			old = item
			old = eval(monkey_ops[mid])
			old = old // 3
			test, pf, nf = monkey_tests[mid]
			monkey_items[nf if old % test else pf].append(old)
		monkey_items[mid].clear()
monkey_counts.most_common(2)


# In[166]:


monkey_counts = Counter()
for _ in range(10000):
	for mid, items in monkey_items.items():
		monkey_counts[mid] += len(items)
		for item in items:
			old = item
			old = eval(monkey_ops[mid])
			old = old % BIGN
			test, pf, nf = monkey_tests[mid]
			monkey_items[nf if old % test else pf].append(old)
		monkey_items[mid].clear()
monkey_counts


# In[167]:


monkey_counts.most_common(2)

