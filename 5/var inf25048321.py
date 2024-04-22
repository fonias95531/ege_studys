def transform(n, i):
    s = ''
    while n>0:
        s = str(n%i)+s
        n = (n-n%i)//3
    return s

def is_posible(n:int):
    s = transform(n, 3)
    if s[-4:-1]=='2101' or s[-3:-1]=='112' or s[-4:-3]==s[-2:-1]:
        return True
    return False


for n in range(133, 500):
    if is_posible(n):
        print(n, transform(n, 3))
        break
