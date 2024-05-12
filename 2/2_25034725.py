from itertools import product
m = [
    [1, 2, 1, 1, 0],
    [2, 2, 0, 0, 1],
    [2, 0, 0, 2, 1]
]


for i in product([1, 0], repeat=4):
    x, y, z, w = i
    f = (x or (not z) or w) and (z or (w != y))
    if f: print(x, z, y, w, f)

'''
x z y w f
1 0 1 0 True
1 1 0 0 1
1 0 0 1 True
0 1 0 1 1
0 0 1 0 True
0 0 0 1 True
'''