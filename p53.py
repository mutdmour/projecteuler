def fac(n):
    product = 1
    for i in range(n, 0, -1):
        product = product * i
    return product

def C(n,r):
    return fac(n) / (fac(r) * fac(n-r))

def main():
    c = 0
    for n in range(1,101):
        for r in range(1,n):
            if C(n,r) > 1000000:
                c = c + 1
    print(c)

main()
