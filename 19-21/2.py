import functools

@functools.lru_cache(None)
def f(a, b, m):
    if 107<=a+b<=170 and m==0: return True
    if m==0 or 107<=a+b<=170: return False
    h = [f(a+10, b, m-1), f(a, b+10, m-1), f(a*2, b, m-1), f(a, b*2, m-1)]
    return any(h) if m%2==1 else all(h)

#  print([s for s in range(1, 100) if f(5, s, 2)]) only any
print([s for s in range(1, 100) if f(5, s, 3)])