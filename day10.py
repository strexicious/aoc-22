#!/usr/bin/env python
# coding: utf-8

# In[38]:


import itertools

with open("day10.txt") as f:
	cycle = -20
	X = 1
	signal_sum = 0
	pixel_buffer = [["."]*40 for _ in range(6)]

	decoded = itertools.chain(*([l] if l[0] == "noop" else [["noop"], l] for l in map(str.split, map(str.strip, f))))
	for l, y, x in zip(decoded, *zip(*itertools.product(range(6), range(40)))):
		cycle += 1
		if not cycle % 40: signal_sum += X * (cycle+20)
		if X-1 <= x <= X+1: pixel_buffer[y][x] = "#"
		if l[0] == "addx": X += int(l[1])

print(signal_sum)
print("\n".join(map("".join, pixel_buffer)))

