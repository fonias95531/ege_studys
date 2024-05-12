from itertools import combinations
from time import time
f = open('27/14405/27A_14405.txt')
n, k = [int(i) for i in f.readline().split()]
s = [int(i) for i in f][::-1]
n = 0
for a in combinations(s, 7):
    if sum(a)%7==0:
        c = 0
        for i in range(len(a)-1):
            c+=int(max(a[i]-k, a[i+1]-k)>min(a[i:i+1]))
        if c==0: 
            if sum(a)>n:
                n = sum(a)
                print(n)
print(n)