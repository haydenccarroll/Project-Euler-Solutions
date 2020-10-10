import time
start = time.time()

def find_abc():
    for c in range(335, 998):
        for b in range(2, c):
            for a in range(1, b):
                if c + b + a == 1000:
                    if b**2 + a**2 == c**2:
                        return a*b*c

print(find_abc())
print("runtime:", time.time()-start)