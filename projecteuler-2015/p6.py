def sumofsquares(n):
    total = 0
    for i in range(n+1):
        total = total + i**2
    return total

def squareofsum(n):
    total = 0
    for i in range(n+1):
        total = total + i
    total = total**2
    return total

def main():
    n = 100
    d = squareofsum(n) - sumofsquares(n)
    print(d)

main()
