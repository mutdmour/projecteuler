def main():
    dic = {}
    l = set()
    for a in range(1,1000):
        l.add(a)
        for b in range(1,1000):
            if not(b in l):
                if a+b <= 1000:
                    c = (a**2 + b**2)**(1/2)
                    if c == int(c):
                        p = a + b + c
                        if p <= 1000:
                            if not(p in dic.keys()):
                                dic[p] = 0
                            dic[p] = dic[p] + 1
    m = 0
    for i in dic.keys():
        if dic[i] > m:
            m = dic[i]
            v = i
    print(v)
main()
