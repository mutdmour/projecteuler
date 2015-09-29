def checkprime(n):
    if n == 3 or n == 2:
        return True # prime
    
    else:
        for i in range (2, int(n**(1/2)+1)):
            t = n / i
            if t == int(t):
                prime = 0
                break
            else:
                prime = 1
        if prime == 1:
            return True
        else:
            return False

def multiplylist(n):
    a = 1
    for i in n:
        a = a * i
    return a

def main():
    r = 600851475143
    x = []
    l = r
    c = 2
    while multiplylist(x) != r:        
        for i in range(c, int(l+1)): #the key here is to remember that the range must include the prime itself, so it would stop when it hits the prime
            if checkprime(i) == True and l % i == 0:
                a = l / i
                x.append(i)
                l = a
                c = i
                break
    print(x[-1])
    
#    for i in range(int(l/2,2,-2):
#        if l%i==0 and checkprime(i):
#            print(i)
#            break

main()
