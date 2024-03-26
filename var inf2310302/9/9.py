f = open('var inf2310302/9/9.txt')
c = [{}, {}, {}, {}, {}, {}]
c1 = f.readline().split()
while c1 != []:
    for i in range(6):
        if c1.count(c1[i])==1:
            try:
                c[i][c1[i]]+=1
            except:
                c[i][c1[i]]=1
    c1 = f.readline().split()
f.close()
c2 = [[], [], [], [], [], []]
for i in range(6):
    for j in c[i]:
        if c[i][j]<170 and j not in c2[i]:
            c2[i].append(j)
            c[i][j] = 0
f = open('var inf2310302/9/9.txt')
c1 = f.readline().split()
while c1 != []:
    for i in range(6):
        if c1[i] in c2[i]:
            c[i][c1[i]]+=1
    c1 = f.readline().split()
f.close()
c2 = [[], [], [], [], [], []]
for i in range(6):
    for j in c[i]:
        if c[i][j]<170 and j not in c2[i]:
            c2[i].append(j)
f = open('var inf2310302/9/9.txt')
c1 = f.readline().split()
rc = 0
while c1 != []:
    c = 0
    for i in range(6):
        if c1.count(c1[i])==1 and c1[i] in c2[i]:
            c+=1
    if c>3:
        rc+=1
    c1 = f.readline().split()
print(rc)
