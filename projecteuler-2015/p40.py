def main():
    c = 0
    prod = 1
    for n in range(1, 1000000):
        n = str(n)
        for i in n:
            c = c + 1
            if c == 1 or c==10 or c==100 or c==1000 or c==10000 or c==100000 or c == 1000000:
                prod = prod * int(i)
            if c == 1000000:
                break
    print(prod)
main()
