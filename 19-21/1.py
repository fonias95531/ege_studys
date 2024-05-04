from functools import lru_cache

end = 231
first_bunch = 10

@lru_cache(None)
def g(a, b, m):
    if b+a>=end: return True
    if m==0: return 0
    m -= 1
    h = [g(a+1, b, m), g(a, b+1, m), g(a*2, b, m), g(a, b*2, m)]
    return all(h) if m%2 else any(h)

print([s for s in range(1, 130) if g(first_bunch, s, 3) and not g(first_bunch, s, 1)])
