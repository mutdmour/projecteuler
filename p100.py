def main():
    tot = 1000000030324+1#10**12
    mx = tot
    mn = 0
    v = 0
    temp = 0
    while v != 1:
        i = mn + int((mx-mn)/2)
        v = 2*(i/tot)*(i-1)/(tot-1)
        if v > 1:
            mx = i
        else:
            mn = i
        if temp == i:
            tot = tot + 1
            mx = tot
            mn = 0
        temp = i
    print(i, tot)
main()
