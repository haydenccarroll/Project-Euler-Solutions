import time
start = time.time()

SIZE = 1001
starting_number = SIZE**2
sum_of_diagonals = starting_number
while starting_number > 0:
    for i in range(4):
        starting_number -= SIZE-1
        if starting_number < 0:
            break
        sum_of_diagonals += starting_number
        print(starting_number)

    SIZE = SIZE-2 if SIZE-2 > 1 else SIZE
    

print(sum_of_diagonals, starting_number)
print('runtime:', time.time()-start)