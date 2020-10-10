import time
start = time.time()

def is_prime(num):
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True

num = 3
prime_list = [2]
while num < 2000000:
    if is_prime(num):
        prime_list.append(num)
    num += 2 
print(prime_list)
print(sum(prime_list))
print("runtime:",time.time()-start)