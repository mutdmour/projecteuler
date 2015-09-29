def multiplyList(n):
    a = 1
    for i in n:
        a = a * int(i)
    return a

def check(s, m, r, l, x, init):
    a = 0 + init
    b = a + l
    c = b + l
    d = c + l
    
    while d != x:
        l = [s[a], s[b], s[c], s[d]]
        t = multiplyList(l)
        if t>m:
            m = t
        a = a + r
        b = b + r
        c = c + r
        d = d + r
    return m
        
        

def main():
    file = open("p11_input.txt", "r")
    s = ""
    for i in file.readlines():
        s = s + i
    s = s.split()
    m = 0
    m = check(s, m, 1, 1, 400, 0)
    m = check(s, m, 1, 20, 400, 0)
    r = 0
    for i in range(80, 420, 20):
        m = check(s, m, 1, 21, i, r)
        r = r + 20
    r = 396
    for i in range(322, 0, -20):
        m = check(s, m, -1, -19, i, r)
        r = r - 20

    print(m)


main()
