file = open('9/25034725/9.txt')
n = 0
for i in file:
    s=list(map(int,i.split()))
    c=0
    for j in s:
        if s.count(j)==1: continue
        if s.count(j)==3 and c<3:
            c+=1
            continue
        else: break
    else:
        if sorted(s)!=s and c==3: n+=1
    if sorted(s)==s: n+=1
print(n)
    
