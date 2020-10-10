#!/usr/bin/env python

import time
start = time.time()

def sum_of_factors(number):
    factors_of_number = []
    for i in range(2, round(number**0.5+1)):
        if number % i == 0:
            factors_of_number.append(i)
            factors_of_number.append(number//i)
    return sum(factors_of_number)+1

def is_amicable(number):
    if sum_of_factors(sum_of_factors(number)) == number and sum_of_factors(sum_of_factors(number)) != sum_of_factors(number):
        return True
    return False

amicable_numbers = []
for i in range(1, 10000):
    if is_amicable(i):
        amicable_numbers.append(i)
print(amicable_numbers)
print(sum(amicable_numbers))
print('runtime:', time.time()-start)

