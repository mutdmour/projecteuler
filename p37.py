def checkprime(x):
    if x == 1:
        return False
    for  i in range(2,int(x**(1/2)+1)):
        if x % i == 0:
            return False
    return True

def truncate(n):
    ans= [n]
    n = str(n)
    r = n
    l = n
    while len(r) != 1:
        r = r[1:len(r)]
        l = l[0:len(l)-1]
        ans.append(int(r))
        ans.append(int(l))
    
    return ans

def main():
    ans = []
    for i in range(8, 1000000):
        if checkprime(i) == True:
            op = truncate(i)
            z = True
            for j in op:
                if checkprime(j) == False:
                    z = False
                    break
            if z == True:
                ans.append(i)
    print(ans)
    print(len(ans))

    tot = 0
    for i in ans:
        tot = tot + i

    print(tot)
    
main()
#truncate(3797)
#print(checkprime (7))
