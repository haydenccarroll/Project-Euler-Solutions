#!/usr/bin/env python

import time
start = time.time()






#pass
#123456789101112131415161718
'''
if 10, does all 1 digits, then first 2 digit
# if 100, does 90/2 == 45

#finds the power of 10, 
    #does that number goes up by that number each time, until it gets to n or passes it
101


'''
#EXPRESS NUIMBER IN POWERS OF 10
def pure_power(x): #represents the change from x to the next increment such as 10 to 20 is 20, if you input 1
    return (x+1)*(10**x)

def to_get_to_point(x): #does not include any digit of 10^x, but everything before it
    list1 = []
    for i in range(1, x+1):
        list1.append(i*(10**i)*.9)
    print(list1)
    return sum(list1)

print(to_get_to_point(2))
print(to_get_to_point(2) + pure_power(2)) #should be rup to point 200


def find_point(x):
    power = len(str(x))-1
    to_get_to_power = to_get_to_point(power)
    return to_get_to_power

    points = []
    for i in str(x):
        points.append(int(i)-1 * pure_power(power))
        power -= 1
    print(points)

print(find_point(12))