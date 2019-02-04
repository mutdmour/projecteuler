def fac(n):
    product = 1
    for i in range(n, 0, -1):
        product = product * i
    return product

def main():
    n = 0
    for i in range(3, 1000000):
        z = False
        d = i
        c = 1
        l = set()
        while z == False:
            tot = 0
            for j in str(d):
                tot = tot + fac(int(j))
            if not(tot in l):
                c = c + 1
                d = tot
                l.add(d)
            else:
                z = True
#                print(i, c)
                if c == 60:
                    n = n + 1
    print(n)

main()
