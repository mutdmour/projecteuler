def pand(n):
    n = str(n)
    for i in range(len(n)):
        j = n[0]
        n = n[1:]
        if (j in n):
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

def main():
    for i in range(10000000-1,0,-1):#8976543201, 0, -2):
        if pand(i) == True:
#            print(i)
 #           if i < 8000000000: #8507264931
#                print("hey",i)
#                break
            if checkprime(i) == True:
                print(i)
                break
            
## using sieve

def sieve(n):
    l = []
    for i in range(3, n+1, 2):
        l.append(i)
    for i in l:
        if i % 2 ==0:
            l.remove(i)
    while len(l) > 0:
        x = l.pop(0)
        for k in l:
            if k%x == 0:
                l.remove(k)
        if pand(x) == True:
            m = x
    print(m)

import time
#start = time.time()
#sieve(1000000) #must be even
#end = time.time()
#print(end-start)

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
 #   print(p)
 #   for i in range(len(p)-1, 0, -1):
#     if pand(p[i]) == True:
#         print(p[i])
#         break


def main2():
    file = open("p41_primes.txt","r")
    for i in file.readlines():
        i = i[:len(i)-1]
        if pand(i) == True:
            print(i)
            break
main2()
        
def comp(a,b):
    if len(str(a)) == len(str(b)):
        for i in str(a):
            if str(b).count(i) != str(a).count(i):
                return False
        return True
    return False

def main():
    n = 3
    i = -1
    cubes = []
    ans = []
    while len(ans) != 3:
        i = i + 1
        ans = [i**3]
        for i in cubes:
            pass

#print(comp(4106375, 66430125))


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

def pand(n):
    n = str(n)
    m = n[0]
    for i in range(len(n)):
        j = n[0]
        n = n[1:]
        if (j in n) or j == "0" or int(j) <= int(m):
            return False
    return True

def main_o():
    for i in range(87643521, 0, -2):
        if pand(i) == True:
            if checkprime(i) == True:
                print(i)
                break

#print(pand(87643511))
#main_o()

def main():
    n = 7
    s = ""
    l = []
    u = 0
    g = 0
 #   v = []
    for i in range(n,0,-1):
        s = s + str(i)
        l.append(i)
        for j in range(n, 0, -1):
            if not(j in l):
                l.append(j)
                s = s + str(j)
                for k in range(n, 0, -1):
                    if not(k in l):
                        s = s + str(k)
                        l.append(k)
                        for m in range(n, 0, -1):
                            if not(m in l):
                                s = s + str(m)
                                l.append(m)
                                for e in range(n, 0, -1):
                                    if not(e in l):
                                        s = s + str(e)
                                        l.append(e)
                                        for o in range(n, 0, -1):
                                            if not(o in l):
                                                s = s + str(o)
                                                l.append(o)
                                                for p in range(n, 0, -1):
                                                    if not(p in l):
                                                        s = s + str(p)
                                                        g = g + 1
                                                        if int(s)%2 != 0:
 #                                                           if g < 50:#g > 3628750 and g < 3628800:
#                                                                       print(s)
#                                                                       g = g + 1
                                                            if checkprime(int(s)) == True:                                                            
#                                                                print(s)
                                                                if int(s) > u:
                                                                    u = int(s)
                                                                                
                                                        s = s[:6]
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
    print(g) #
    print(u)

main()

