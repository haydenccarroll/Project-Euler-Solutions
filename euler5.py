import time
start = time.time()

def is_multiple(num):
    for i in range(2,20):
        if num % i != 0:
            return False
    return True

def find_lowest_multiple():
    num = 0
    while True:
        num += 19
        if is_multiple(num):
            return num
        


print(find_lowest_multiple())
print("runtime:", time.time()-start)