def div(x):
    cyc = ""
    ans = []
    rem = []
    r = 10
        
    while r != 0 and not(r in rem):
        rem.append(r) #the position of this matters, for example, I think 4
        while r < x:
            r = r * 10
            ans.append(0)
            rem.append(10) #this is key, for example, 12
        a = r%x
        b = r//x
        ans.append(b)
        r = a * 10
#        print(b,ans)

 #   print(r, rem)
#    print(ans)
    if r in rem:
        pos = rem.index(r)
        for i in range(pos,len(ans)):
            cyc = cyc + str(ans[i])
#    print(ans, "cyc:", cyc)
    return len(cyc)

def main():
    m = 0
    for i in range(2,999):
        if div(i) > m:
            m = i
    print(m)

main()
