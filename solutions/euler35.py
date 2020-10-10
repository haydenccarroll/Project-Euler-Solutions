#!/usr/bin/env python

import time
start = time.time()

def is_prime(num):
    if num % 2 == 0 and num != 2:
        return False
    for i in range(3, int(num**.5)+1, 2):
        if num % i == 0:
            return False
    return True

def all_rotations(num):
    num = list(str(num))
    rotations = []
    for i in range(len(num)):
        num.insert(0, None)
        num[0] = num[-1]
        num.pop()
        rotations.append(int(''.join(num)))
    return rotations

def all_rotations_prime(num):
    for i in all_rotations(num):
        if not is_prime(i):
            return False
    print(num)
    return True

counter = 0
num = 2
while num < 1000000:
    if all_rotations_prime(num):
        counter += 1
    num += 1
print(counter)

print('runtime:', time.time()-start)