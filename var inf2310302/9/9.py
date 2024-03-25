f = open('var inf2310302/9/9.txt')
c = [{}*6]
c1 = f.readline().split()
while c1 != []:
    for i in c1:
        if c1.count(i)==1:
            try:
                c[0][c1[0]]+=1
            except:
                c[0][c1[0]]=1
for i in c:
    for j in i:
        if i[j]<170:
            pass
    