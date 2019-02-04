def checkprime(x):
    if x == 1:
        return False
    for  i in range(2,int(x**(1/2)+1)):
        if x % i == 0:
            return False
    return True

def main():
    z = True
    i = 1
    prime = []
    while z == True:
        i = i + 2
        if checkprime(i) == True:
            prime.append(i)
        else:
            for j in prime:
                dif = i - j
                k = dif/2
                if int(k) == k and int(k**(1/2))==(k**(1/2)):
 #                   print(i, j,k**(1/2))
                    z = True
                    break
                z = False
    print(i)                                                  

main()
            
