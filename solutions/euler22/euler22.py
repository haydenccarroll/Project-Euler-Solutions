import time
start = time.time()

with open('names.txt', 'r') as namesFile:
    name_string = namesFile.read()

alpha_to_int = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

name_list = name_string.split(",")
for index, name in enumerate(name_list):
    new_name = []
    for char in name:
        if char != '"':
            new_name.append(alpha_to_int.index(char))
    name_list[index] = new_name
name_list = sorted(name_list)

running_total = 0
for index, name in enumerate(name_list):
    running_total += sum(name) * (index+1)

print(running_total)
print('runtime:', time.time()-start)