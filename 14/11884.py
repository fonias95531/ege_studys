for x in range(0, 12):
    s = int('9a87021', 12) + int('2068', 14) + int('102f4', 16) + (int('100', 12)+int('100', 14))*x
    if s%3==0:
        print(x)