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
    z = False
    for i in range(11, 1000000):
        for j in str(i):
            if str(i).count(j) >= 2:
                if checkprime(i) == True:
                    l = set()
                    for m in range(0,10):
                        rep = str(i)
                        for k in range(len(rep)-1):
                            if rep[k] == j:
                                rep = rep[:k] + "{0}".format(m) + rep[k+1:]
                        if checkprime(int(rep)) == True:
                            if len(str(int(rep))) == len(str(i)):
                                l.add(int(rep))
                    if len(l)==8:
                        print(i)
                        z = True
                        break
        if z == True:
            break
                                
main()
