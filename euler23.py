import time
start = time.time()

def is_abundant(number):
    factors_of_number = []
    for i in range(2, round(number**0.5+1)):
        if number % i == 0:
            factors_of_number.append(i)
            if number // i != i:
                factors_of_number.append(number//i)
    if sum(factors_of_number)+1 > number:
        return True
    return False

def can_be_summed_checker(number):
    for number_1 in abundant_list:
        for number_2 in abundant_list:
            if number_1 + number_2 == number:
                return True
            if number_1 + number_2 > number:
                break
        if number_1 > number:
            break
    return False
abundant_list = [x for x in range(1, 28214) if is_abundant(x)]
cannot_be_summed_list = []
#how to check through list to see if a number cant be found by sum of two abundant numbers
for number in range(1,28214):
    if not can_be_summed_checker(number):
        cannot_be_summed_list.append(number)



print('runtime:', time.time()-start)