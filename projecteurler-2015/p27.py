def checkprime(x):
    if x == 1 and x%2 == 0:
        return False
    for  i in range(3,int(x**(1/2)+1),2):
        if x % i == 0:
            return False
    return True

def main():
    m = 0
    for a in range(-999, 999, 2):
        for b in range(-999, 999, 2):
            n = 0
            z = True
            c = 0
            while z == True:
                v = n**2 + a * n + b
                if checkprime(abs(v)) == True:
                    c = c + 1
                    n = n + 1
                else:
                    if c > m:
 #                       print(a,b,c)
                        p = a * b
                       # a_m = a
#                        b_m = b
#                        c_m = c
                        m = c
                    z = False
    print(p)
main()
