#!/usr/bin/env python

import time
start = time.time()

highest_loop = 0
highest_number = 0
list_of_collatz = []
for starting_number in reversed(range(1,1000000)):
    n = starting_number
    loop_count = 1
    while n != 1:
        n = 3*n+1 if n % 2 == 1 else n/2
        loop_count += 1
    highest_loop = loop_count if loop_count > highest_loop else highest_loop
    if highest_loop == loop_count:
        highest_number = starting_number
    
    
print(highest_loop)
print(highest_number)
print('runtime:',time.time()-start)