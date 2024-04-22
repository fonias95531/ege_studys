for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((x==y)<=(not bool(z) or w)) == (not ((w<=x) or (y<=z)))
                if f:
                    print(x, y, z, w)
