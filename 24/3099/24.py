f = open('24/3099/24_3099.txt')
s = f.readline()
b = {}
for i in s:
    try: b[i]+=1
    except: b[i]=1
c = 0
for i in b:
    if b[i]%2==1:
        c+=1
print(c//2)