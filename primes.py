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

def isprime(n):
    import math
    p = primes(math.sqrt(n))
    for i in p:
        if n % i == 0:
            return False
    return True

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

import time
start = time.time()
print(isprime(8507429163))
end = time.time()
print(end-start)

start = time.time()
print(checkprime(8507429163))
end = time.time()
print(end-start)

