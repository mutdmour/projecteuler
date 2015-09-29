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
    v = 3
    per = 100
    l = 1
    n = 0
    while per > 10:
        v = v+2
        k = v**2
#        d = [v**2]
        dif  = v - 1
        while k != l:
#            print(d)
            for i in range(4):
                k = k - dif
#                d.append(k)
                if checkprime(k) == True:
                    n = n + 1
            dif = dif - 2
        per = n / (v*2-1) * 100
 #       print(d, per)
        l = v**2
    print(v)
        
main()
