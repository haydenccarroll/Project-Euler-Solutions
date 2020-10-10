#!/usr/bin/env python

import time
start = time.time()
sum_of_squares = sum([x**2 for x in range(1,101)])
square_of_sum = sum([x for x in range(1,101)])**2

print(square_of_sum - sum_of_squares)
print("runtime:", time.time()-start)