#!/usr/bin/env python

import time
import math
start = time.time()



def is_prime(n):
    for i in range(3, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


def is_pan(n):
    strn = str(n)
    for i in range(1, max([int(x) for x in strn])+1):
        if str(i) not in strn:
            return False
    return True


print(is_pan(1235))

def funct():
    i = 987654321
    current_max = 0
    while i < 1000000000:
        if is_pan(i) and is_prime(i):
            break
        i -= 2
    print(i)
    
funct()

987654321

#find pandigitals first
