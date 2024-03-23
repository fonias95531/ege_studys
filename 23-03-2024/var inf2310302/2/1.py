for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x == z) <= (not bool(y) or w)) == (not((w <= z) or (x <= y)))
                if f:
                    print(x, y, z, w)
