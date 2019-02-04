def pand(n):
#    n = str(n)
    for i in range(len(n)):
        j = n[0]
        n = n[1:]
        if (j in n):
            return False
    return True

def main():
    tot = 0
    for n in range(100000000, 1000000000-1):
        n = str(n)
        if pand(n) == True:
 #           print(n)
            v = [2,3,5,7,11,13,17]
            z = True
            for i in range(0,len(n)-2):
                ss = (int(n[i]+n[i+1]+n[i+2]))
                #print(ss, v[i-1])
                if ss % v[i] != 0:
                    z = False
                    break
            if z == True:
 #               print(n)
                for i in range(0,10):
                    i = str(i)
                    if not (i in n):
                        n = i + n
                print(n)
                tot = tot + int(n)
 #           break
    print(tot)

def checkprop(n):
    n = str(n)
    v = [2,3,5,7,11,13,17]
    for i in range(1,len(n)-2):
        ss = (int(n[i]+n[i+1]+n[i+2]))
#        print(ss)
        if ss % v[i-1] != 0:
            return False
    return True

def main2():
    n = 9
    s = ""
    l = []
    g = 0
    tot = 0
    for i in range(n,-1,-1):
        s = s + str(i)
        l.append(i)
        for j in range(n, -1, -1):
            if not(j in l):
                l.append(j)
                s = s + str(j)
                for k in range(n, -1, -1):
                    if not(k in l):
                        s = s + str(k)
                        l.append(k)
                        for m in range(n, -1, -1):
                            if not(m in l):
                                s = s + str(m)
                                l.append(m)
                                for e in range(n, -1, -1):
                                    if not(e in l):
                                        s = s + str(e)
                                        l.append(e)
                                        for o in range(n, -1, -1):
                                            if not(o in l):
                                                s = s + str(o)
                                                l.append(o)
                                                for p in range(n, -1, -1):
                                                    if not(p in l):
                                                        s = s + str(p)
                                                        l.append(p)
                                                        for q in range(n, -1, -1):
                                                            if not(q in l):
                                                                s = s + str(q)                                                
                                                                l.append(q)
                                                                for r in range(n, -1, -1):
                                                                    if not(r in l):
                                                                        s = s + str(r)
                                                                        l.append(r)
                                                                        for t in range(n, -1, -1):
                                                                            if not(t in l):
                                                                                s = s + str(t)
                                                                                #print(s)
                                                                                if checkprop(s) == True:
                                                                                    print(s)
                                                                                    tot = tot + int(s)
                                                                                g = g + 1
                                                                                

                                                                        s = s[:8]
                                                                        l.remove(r)
                                                                s = s[:7]
                                                                l.remove(q)
                                                        s = s[:6]
                                                        l.remove(p)
                                                s = s[:5]
                                                l.remove(o)
                                        s = s[:4]
                                        l.remove(e)
                                s = s[:3]
                                l.remove(m)
                        s = s[:2]
                        l.remove(k)
                s = s[:1]
                l.remove(j)
        l.remove(i)
        s = ""
#    print(g)
    print(tot)
main2()
#print(checkprop(9876543210))
