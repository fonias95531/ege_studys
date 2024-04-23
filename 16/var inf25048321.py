l = [1]
for i in range(1, 2024):
    l.append(i-2+l[i-1])
print(l[2023]-l[2021])