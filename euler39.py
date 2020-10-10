import time
import math

start = time.time()

#law of cosines: a^2 = b^2 + c^2 -2bcCosA
#((a^2)-(b^2 + c^2)) / -2bc

def is_solution(a, b, c): #nope needs to be right anglke
    angles = sorted([a,b,c])
    if angles[2]**2 == angles[1]**2 + angles[0]**2:
        return True
    return False


def potential_solutions(p):
    solutions = set()
    for a in reversed(range(p//3+1, p)):
        for b in range(1, min([p-a, a])):
            c = p-a-b
            if c > b or b > a:
                print('we fraked up at ', a,b,c)
            if is_solution(a, b, c):
                solutions.add(tuple(sorted([a, b, c])))
    return len(solutions)

highest = [0,0]
for i in range(1, 1001):
    x = potential_solutions(i)
    highest = [x,i] if x > highest[0] else highest
print(highest)
print('runtime:', time.time()-start)