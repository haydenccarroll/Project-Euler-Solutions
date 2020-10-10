#!/usr/bin/env python

import time
start = time.time()

def is_double_palindrome(num):
    if str(num) == str(num)[::-1] and str(bin(num))[2:]== str(bin(num))[:1:-1]:
        return True
    return False

num = 0
list_to_sum = []
while num < 1000000:
    if is_double_palindrome(num):
        list_to_sum.append(num)
    num += 1

print(sum(list_to_sum))



print('runtime:', time.time()-start)