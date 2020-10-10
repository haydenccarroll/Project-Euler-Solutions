#!/usr/bin/env python

import time
start = time.time()

def over_fivehundred_factors(num):
    factor_count = 2
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            factor_count += 2
    if factor_count > 500:
        return True
    return False

triangle_number = 0
i = 1
while not over_fivehundred_factors(triangle_number):
    triangle_number += i
    i += 1
print(triangle_number)
print('runtime:',time.time()-start)