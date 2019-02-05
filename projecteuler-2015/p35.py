def checkprime(x):
    for  i in range(2,int(x**(1/2)+1)):
        if x % i == 0:
            return False
    return True

def rotate(x):
    t = x[1:len(x)] + x[0]
    ans = [x, t]
    while t != x:
        t = t[1:len(x)] + t[0]
        if not(t in ans):
            ans.append(t)
    return ans

def main():
    ans=[]
    for i in range(2, 1000000):
        if checkprime(i) == True:
            l = rotate(str(i))
            for j in l:
                z = True
                if checkprime(int(j)) == False:
                    z = False
                    break
            if z == True:
                ans.append(i)
 #   print(ans)
    print(len(ans))
    
main()
#print(rotate("197"))
