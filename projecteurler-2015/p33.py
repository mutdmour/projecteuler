def main():
    import fractions
    i = 10
    prodn = 1
    prodd = 1
    count = 0
    while count != 4:
        i = i + 1
        for j in range(i+1,100):
            thefloat = i / j
            a=[]
            for m in str(i):
                a.append(m)
            b=[]
            for m in str(j):
                b.append(m)
            n = len(a)
            z = False
            for k in range(n):
                for m in range(len(b)):
                    if a[k] == b[m] and not(a[k]=="0"):
                        a.pop(k)
                        b.pop(m)
                        z = True
                        break
                if z == True:
                    c = ""
                    d = ""
                    for m in a:
                        c = c + m
                    for m in b:
                        if (m != "0"):
                            d = d + m
                        else:
                            d = d + "1"
                    thefrac = int(c)/int(d)
                    if thefrac == thefloat:
                        prodn = prodn * int(c)
                        prodd = prodd * int(d)
                        count = count + 1
                        print(i,j)
                        print(c,d)
                    break
    print(prodn, prodd)

main()
