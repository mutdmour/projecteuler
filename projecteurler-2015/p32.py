def pand(n):
    n = str(n)
    for i in range(len(n)):
        j = n[0]
        n = n[1:]
        if (j in n) and j == 0:
            return False
    return True

def compare(a,b):
    a = str(a)
    b = str(b)
    for i in a:
        if i in b:
            return False
    return True

def pand19(a,b):
    m = a * b
    n = str(a) + str(b) + str(m)
    for i in range(len(n)):
        j = n[0]
        n = n[1:]
#        print(j,n)
        if (j in n) or j == "0":
            return False
    return True

def main():
    l = set()
    tot = 0
    for a in range(100):
        for b in range(10000):
            m = a * b
            n = len(str(a))+len(str(b))+len(str(m))
            if n >9:
                break
            elif n == 9:
 #               print(a,b,m)
                if pand19(a,b) == True and not(m in l):
 #                   print(a,b,m)
                    l.add(m)
                    tot = tot + m
    print(tot)

main()
#print(pand(12434))
#print(compare(1234, 56718))
#print(pand19(32,169))
