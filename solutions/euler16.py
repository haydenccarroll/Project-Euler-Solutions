#!/usr/bin/env python

import time
start = time.time()

num = str(2**1000)
answer = sum([int(x) for x in num])
print(answer)
print('runtime:',time.time()-start)