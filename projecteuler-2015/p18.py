def find(main, lpos, spos, mx, dif):
    if lpos == len(main):
        return 0
    l = main[lpos]
    s = l[spos]
    print(s)
    tot = s + find(main, lpos+1, 0, mx, dif)
    if tot > mx:
        mx = tot
        print(mx)
    tot = tot - s
    lpos = lpos - dif
    dif = dif + 1
    return find(main, lpos, 1, mx, dif)

def main():
    file = open("p18_input.txt", "r")
    main = []
    for i in file.readlines():
        sub = i.split()
        for j in range(len(sub)):
            sub[j] = int(sub[j])
        main.append(sub)
    print("mx", find(main, 0, 0, 0, 0))
main()
