def factorial(n):
    product = 1
    for i in range(n, 0, -1):
        product = product * i
    return product

def main():
    summ = 0
    for n in range(3,100000):
        n = str(n)
        tot = 0
        for i in n:
            i = int(i)
            tot = tot + factorial(i)
        if tot == int(n):
            summ = summ + tot
    print(summ)

main()
