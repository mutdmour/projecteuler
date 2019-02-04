def main():
    c = 1
    m = 0
    for i in range(6, 7):
        l = [0, 1]
        for r in range(2,i):
            l.append(r)
        for j in l:
            if j != 0:
                if i % j == 0:
                    k = j
                    while k < i:
                        l[k] = 0
                        k = k + j
        print(i, l)
        v = i / len(l)
        if v > m:
            m = v
            m_i = i
    print(m_i, m)

main()
