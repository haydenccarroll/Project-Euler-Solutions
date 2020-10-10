#!/usr/bin/env python

import time
start = time.time()

running_product = 1
for number in range(2,100):
    if number % 10 == 0:
        running_product *= number//10
        continue
    running_product *= number
running_product = str(running_product)
print(running_product)
list_of_digits = [int(i) for i in running_product]
print(sum(list_of_digits))


print('runtime:', time.time()-start)
