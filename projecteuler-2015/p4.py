def reverse(n):
    a = ""
    for i in range(len(n)-1, -1, -1):
        a = a + n[i]
    return a

def findmax(n):
    m = n[0]
    for i in n:
        if i > m:
            m = i
    return m

def checkpalindrome(n):
    r = reverse(n)
    for i in range(len(n)):
        if r[i] == n[i]:
            pass
        else:
            return False
    return True
    

def main():
    z = False
    l = []
    for i in range(999, 99, -1):
        for j in range(999,99,-1):
            k = i*j
            if checkpalindrome("{0}".format(k)) == True:
                l.append(k)
    print(findmax(l))
                
main()
