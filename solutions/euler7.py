#!/usr/bin/env python

import time
start = time.time()

def is_prime(num):
        for i in range(2,num//2+1):
            if num % i == 0:
                return False
        return True
prime_count = 1
num = 3
while prime_count < 10001:
    if is_prime(num):
        prime_count += 1
    num += 2


print(num-2)
print('runtime:', time.time()-start)