import time
import re
start = time.time()

def shift_r(list1):
    start_list = list(list1)
    index_to_use = [m.start(0) for m in re.finditer(r'r[d]+', list1)]
    print(index_to_use)
    list1[index_to_use] = 'd'
    list1[index_to_use+1] = 'r'
    if start_list == list1:
        return False
    return list1
list1 = 'rrdd'
list_of_stuff = [list1]
while shift_r(list(list1)):
    list1 = shift_r(list(list1))
    list_of_stuff.append("".join(list1))

for i in list_of_stuff:
    print(i)

print(len(list_of_stuff))
amount_of_turns = 4
r_total = amount_of_turns // 2
d_total = amount_of_turns // 2
list_of_permutations = [[]]
for i in range(r_total):
    list_of_permutations[-1].append('r')
for i in range(d_total):
    list_of_permutations[-1].append('d')




print('runtime:',time.time()-start)