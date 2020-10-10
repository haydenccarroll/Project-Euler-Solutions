import time
from fractions import Fraction
from functools import reduce
start = time.time()
list1 = []
for a in range(10, 100):
    for b in range(10, 100):
        quotient = 0
        if a % 10 == 0 and b % 10 == 0:
            continue
        str_a, str_b = str(a), str(b)
        if str_a[0] in str_b:
            str_b = list(str_b)
            str_b.remove(str_a[0])
            str_b = "".join(str_b)
            try:
                quotient = int(str_a[1])/int(str_b)
            except ZeroDivisionError:
                pass
        elif str_a[1] in str_b:
            str_b = list(str_b)
            str_b.remove(str_a[1])
            str_b = "".join(str_b)
            try:
                quotient = int(str_a[0])/int(str_b)
                #print(a/b, quotient, str_b)
            except ZeroDivisionError:
                pass
        if quotient == a/b and a < b:
            list1.append([a, b])
numerator = reduce((lambda x, y: x * y), [x[0] for x in list1])
denominator = reduce((lambda x, y: x * y), [x[1] for x in list1])
print(Fraction(numerator, denominator).denominator)
print('runtime:', time.time()-start)