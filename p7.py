def checkprime(n):
    if n == 3 or n == 2:
        return True # returns true if prime
    
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
            return False #returns false if not prime

def main():
    l = [1,2]
    n = 1
    while len(l) != 10002:
        n = n + 2
        if checkprime(n) == True:
            l.append(n)
    print(l[-1])

main()
