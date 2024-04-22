s = [1, 2, 3, 4, 5, 6, 7, 8]
for i in range(11):
    s2 = []
    for s1 in s:
        s2.extend([x for x in range(int(s1)+1, 9, 2)] + [x for x in range(int(s1)-2, -1, -2)])
    s = s2
    print(len(s))
print(len(s))