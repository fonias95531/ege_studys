from functools import lru_cache
import time

@lru_cache(None)
def f(s):
    for i in range(len(s)-6):
        c = s[i:i+7]
        if c==c[::-1]: return 1
        for h in range(len(c)):
            for j in range(len(c)):
                a = list(c)
                a[h], a[j] = a[j], a[h]
                if a==a[::-1]: return 1
    return 0

s = time.time()
j = 0
file = open('24/3091/24__3091.txt')
for i in file:
    j+=f(i)
print(j, time.time()-s)