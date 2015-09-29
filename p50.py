def primes(n):
    import math
    p = [0, 2]
    n = math.floor(n)
    for i in range(3,n+1,2):
        p.append(i)
 #   print(p)
    q = len(p)
    ub = math.floor(math.sqrt(n))
 #   print(ub)
    for k in range(3, ub+1, 2):
        if p[int((k+1)/2)] != 0:
            for i in range(int((k*k+1)/2),q,k):
#                print(i, p[i])
                p[i] = 0;
#    print(p)
    while 0 in p:
        p.remove(0)
        
    return p
 #   print(p)


def main(p):
  #  p = primes(991)
    m = 0
    for i in range(len(p)-1,-1, -1):
        for j in range(0, len(p)-1):
#            print(p[j])
            n = p[i]
            k = j
            l = []
            while n != 0 and k > -1 and n > -1:
                n = n - p[k]
                l.append(p[k])
                k = k + 1
#            print(l, len(l))
#            print(n)
            if n == 0:
                if len(l) > m:
                    m = len(l)
                    m_v = p[i]
                    m_l = l
                    break
        break
    print(m_v)
    print(m_l)

#def read():
#    file = open("p50_primes.txt", "r")
    
