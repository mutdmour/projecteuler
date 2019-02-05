def expressions(a,b,c,d):
    l = ("+", "-", "*", "/")
    r = (a, b, c, d)
    ans = set()
    for i in l:
        for j in l:
            for k in l:
                for m in r:
                    d = set()
                    d.add(m)
                    for n in r:
                        if not(n in d):
                            d.add(n)
                            for o in r:
                                if not(o in d):
                                    d.add(o)
                                    for p in r:
                                        if not(p in d):
                                            v = eval("{3} {0} {4} {1} {5} {2} {6}".format(i, j, k, m, n, o, p))
                                            v1 = eval("({3} {0} {4}) {1} {5} {2} {6}".format(i, j, k, m, n, o, p))
                                            if "({3} {0} {4} {1} {5})".format(i, j, 0, m, n, o, 0) != 0:
                                                v2 = eval("({3} {0} {4} {1} {5}) {2} {6}".format(i, j, k, m, n, o, p))
                                            v3 = eval("{3} {0} {4} {1} ({5} {2} {6})".format(i, j, k, m, n, o, p))
                                            if eval("({4} {1} {5} {2} {6})".format(0, j, k, 0, n, o, p)) != 0:
                                               # print("{3} {0} ({4} {1} {5} {2} {6})".format(i, j, k, m, n, o, p))
                                                v4 = eval("{3} {0} ({4} {1} {5} {2} {6})".format(i, j, k, m, n, o, p))
                                            v5 = eval("{3} {0} ({4} {1} {5}) {2} {6}".format(i, j, k, m, n, o, p))
                                            v6 = eval("({3} {0} {4}) {1} ({5} {2} {6})".format(i, j, k, m, n, o, p))

                                            t = (v, v1, v2, v3, v4, v5, v6)

                                            for g in t:
                                                if g == int(g) and g > 0:
                                                    ans.add(int(g))
                                    d.discard(o)
                            d.discard(n)
 #   print(ans)
#    print(len(ans))
    z = True
    i = 1
    c = 0
    while z == True:
        if i in ans:
            c = c + 1
            i = i + 1
        else:
            z = False

#    print(c)
    return c
            

#expressions(1,2,3,4)

def main():
    m = 0
    for i in range(9, 0, -1):
        for j in range(i, 0, -1):
            for k in range(j, 0, -1):
                for l in range(k, 0, -1):
                    c = expressions(i, j, k, l)
                    if c > m:
                        m = c
                        ans = "{0}{1}{2}{3}".format(l,k,j,i)
    print(ans)

import time
st = time.time()
main()
end = time.time()
print(end - st)
