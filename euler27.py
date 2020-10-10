import time
start = time.time()

def is_prime(n):
    if n % 2 == 0:
        return False
    try:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
    except TypeError: #is negative, no negatives are prime
        return False
    return True

def testing_function(a, b):
    n = 0
    prime_count = 0
    while is_prime(n**2 + a*n + b):
        prime_count += 1
        #print(n, n**2 + a*n + b, prime_count)
        n += 1
    return prime_count

#testing_function(-79, 1601)

highest_prime_count = 0
ab_product = 0

for a in range(-999, 1000):
    for b in range(-1000, 1001):
        current_test = testing_function(a, b)
        if current_test > highest_prime_count:
            highest_prime_count = current_test
            ab_product = a * b
print(ab_product)

print('runtime:',time.time()-start)