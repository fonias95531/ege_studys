for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x or not y) and (y != z) and not bool(w)
                if f:
                    print(x, y, z, w, f)