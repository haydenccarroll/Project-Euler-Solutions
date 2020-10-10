#!/usr/bin/env python

import time
start = time.time()

def is_prime(num):

    if num % 2 == 0 and num != 2:
        return False
    
    if num == 1:
        return False
    
    for i in range(3, int(num**.5)+1, 2):
        if num % i == 0:
            return False
    return True

def is_truncatable_prime(num):

    for i in range(len(str(num))):
        print(int(str(num)[i:]))
        if is_prime(int(str(num)[i:])) == False:
            return False

    num = list(str(num))
    for i in range(len(num)-1):
        num.pop()
        if is_prime(int("".join(num))) == False:
            return False
            
    return True


num = 11
truncatable_primes = []

while len(truncatable_primes) < 11:
    if is_truncatable_prime(num):
        truncatable_primes.append(num)
        #print(num)
    num += 2

print(truncatable_primes)
print(sum(truncatable_primes))
print('runtime:', time.time()-start)


