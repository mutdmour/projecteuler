def factorial(n):
    product = 1
    for i in range(n, 0, -1):
        product = product * i
    return product

def sumdigits(n):
    n = str(n)
    total = 0
    for i in n:
        total = total + int(i)
    return total

def main():
    print(sumdigits(factorial(100)))

main()
