import time
start = time.time()

i = 2
total_sum = 0
for i in range(2, 1000000):
    the_sum = sum([int(str(i)[z])**5 for z in range(len(str(i)))])
    if the_sum == i:
        print(the_sum)
        total_sum += the_sum
    i += 1

print(total_sum)
print('runtime:', time.time()-start)

