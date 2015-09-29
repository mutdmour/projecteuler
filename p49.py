def checkprime(x):
    if x == 1:
        return False
    for  i in range(2,int(x**(1/2)+1)):
        if x % i == 0:
            return False
    return True

def anagrams(s):
    if s == "":
        return[s]
    else:
        ans = []
        for w in anagrams (s[1:]):
            for pos in range(len(w)+1):
                ans.append(w[:pos] + s[0] + w[pos:])
        return ans

def main():
    for i in range(1000, 10000):
        if checkprime(i) == True:
            if len(str(i)) == 4:
                l = anagrams(str(i))
                so = []
                for j in l:
                    if checkprime(int(j)) == True:
                        so.append(j)

                ans = []
                for k in range(len(so)):
                    r = int(so[k])
                    if not(r in ans) and r >= i:
                        ans.append(r)
                ans.sort()
 #               print(ans)
                if len(ans)>2:
                    v = ans[0]
                    ans = ans[1:len(ans)]
#                    print(ans)
                    
                    for j in ans:
                        dif = j - v
                        if j+dif in ans:
                            st = str(v)+str(j)+str(j+dif)
                            print(i, st, dif)
                            break
                
#main()               
print(anagrams("210"))
#print(checkprime(1487))
