#!/usr/bin/env python

import time
start = time.time()
'''
    we have 2 3digit numbers

    start with 999 x 999, go to 999 x 998 go to 999 x 997
        if that doesnt work, go to 998x999 go to 998x998
            for each thing, test if it is a palindrome


graph of 999 * 999 998*999



'''



def is_palindrome(number):
    number = str(number)
    if number == number[::-1]:
        return True
    return False

palindrome_list = []
for i in range(1, 1000):
    for z in range(1, 1000):
        if is_palindrome(i*z): palindrome_list.append(i*z)

print(sorted(palindrome_list)[-1])
print('runtime:',time.time()-start)