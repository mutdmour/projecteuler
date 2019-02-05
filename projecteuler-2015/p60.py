def primes(n):
    import math
    p = [0, 2]
    n = math.floor(n)
    for i in range(3,n+1,2):
        p.append(i)
    q = len(p)
    ub = math.floor(math.sqrt(n))
    for k in range(3, ub+1, 2):
        if p[int((k+1)/2)] != 0:
            for i in range(int((k*k+1)/2),q,k):
                p[i] = 0;
    while 0 in p:
        p.remove(0)
        
    return p

def checkprime(x):
    if x == 1:
        return False
    elif x == 2:
        return True
    elif x%2 == 0:
        return False
    for  i in range(3,int(x**(1/2)+1),2):
        if x % i == 0:
            return False
    return True

def test(a,b, p):
    a, b = str(a), str(b)
    r = a + b
    s = b + a
    r, s = int(r), int(s)
    if r > p[len(p)-1]:
        if checkprime(r) == False:
            return False
    elif not(r in p):
        return False
    if s > p[len(p)-1]:
        if checkprime(s) == False:
            return False
    elif not(s in p):
        return False
    return True

def main():
    n = 5
    p = primes(8400)
    print('hey')
    for i in range(1, len(p)):
        l = []
        for j in range(i):
            if test(p[i],p[j],p):
                z = True
                for k in l:
                    if test(p[j], k, p) == 0:
                        z = False
                        break
                if z == True:
                    l.append(p[j])
        l.append(p[i])
        tot = 0
        if len(l) == n:
            for j in l:
                tot = tot + j
            break
    print(tot)
    print(p[i])

main()
