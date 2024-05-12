for n in range(3, 10000):
    s = '5'+'2'*n
    while s.find('52')!=-1 or s.find('2222')!=-1 or s.find('1122')!=-1:
        s = s.replace('52', '11', 1)
        s = s.replace('2222', '5', 1)
        s = s.replace('1122', '25', 1)
    if sum(map(int, s))==64:
        print(n)