def main():
    ans = {}
    for n in range(1,100000):
        st = ""
        i = 0
        while len(st)!=9:
            i = i + 1
            m = str(n * i)
            for j in m:
                z = True
                if not (j in st) and not(j == "0"):
                    st = st + str(j)
                else:
                    z = False
                    break
            if z == False:
                break
        if z == True:
            ans[n] = st
            
    m = 0
    for i in ans.values():
        if int(i) > m:
            m = int(i)
    print(ans)
    print(m)
    
main()
