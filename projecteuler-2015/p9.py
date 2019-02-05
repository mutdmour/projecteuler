z = False
for c in range(1,1000):
    for b in range(1,c):
        for a in range(1,b):
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print(a*b*c)
                    z = True
                    break
        if z == True:
            break
    if z == True:
        break

