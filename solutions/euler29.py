#!/usr/bin/env python

import time
start = time.time()

my_set = set()
for a in range(2, 101):
    for b in range(2, 101):
        my_set.add(a**b)
print(len(my_set))


print('runtime:', time.time()-start)