def main(x):
    n = 2 ** x
    n = str(n)
    total = 0
    for i in n:
        total = total + int(i)
    print(total)

