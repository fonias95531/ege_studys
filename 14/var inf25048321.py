for i in '01234567':
    n = int(i)*(256+64*8+9)+16+3*64+3
    while n!=2 and n>0:
        if n%2==1:
            break
        n//=2
    if n==2:
        print(i)