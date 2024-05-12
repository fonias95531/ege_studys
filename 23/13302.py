from functools import lru_cache

start = '1'
@lru_cache(None)
def f(n):
    if n=='101000101': return 1
    elif int(n, 2)> int('101000101', 2): return 0
    h = [f(bin(int(n, 2)+1)[2:]), f(n+bin(int(n, 2)%5)[2:])]
    return sum(h)
print(f(start))
