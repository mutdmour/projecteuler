def main():
    import fractions

    l = []
    n = 0
    while len(l) != 100-1:
        l.append(1)
        n = n + 2
        l.append(n)
        l.append(1)

    l.reverse()
    #print(l)
    k = l.pop(0)
    for i in l:
        k = fractions.Fraction(i + 1 / k)
    k = fractions.Fraction(2+1/k)
    k = str(k)

    tot = 0
    for i in k:
        if i == "/":
            break
        tot = tot + int(i)
    print (tot)

main()
