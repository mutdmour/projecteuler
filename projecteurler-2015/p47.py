def checkprime(x):
    if x == 1:
        return False
    for  i in range(2,int(x**(1/2)+1)):
        if x % i == 0:
            return False
    return True

def fac(n, prime):
    l = set()
    for i in prime:
        while n%i ==0:
            n = n/i
            l.add(i)
    return (len(l))

def main():
    z = True
    i = 1
    prime=[]
    while z == True:
        i = i + 1
        j = i + 1
        k = j + 1
        m = k + 1
        
        i_p = checkprime(i)
        j_p = checkprime(j)
        k_p = checkprime(k)
        m_p = checkprime(m)

        if i_p == True:
            prime.append(i)
        if j_p == True:
            prime.append(j)
        if k_p == True:
            prime.append(k)
        if m_p == True:
            prime.append(m)

        if i_p == False:
            if fac(i,prime) == 4:
                if j_p == False:
                    if fac(j,prime) == 4:
                        if k_p == False:
                            if fac(k,prime) == 4:
                                if m_p == False:
                                    if fac(m,prime) == 4:
                                        z = False

    print(i)


main()

#fac(14,[2,3,5,7,11,13])#,17,19,23])
