#!/usr/bin/env python

import time
start = time.time()


def is_prime(num):
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True


def find_largest_prime_factor(num):
    for i in (range(3, num//2+1, 2)):
        if num % i != 0:
            continue
        if is_prime(num//i):
            return num//i


print(find_largest_prime_factor(600851475143))
print("runtime:", time.time()-start)