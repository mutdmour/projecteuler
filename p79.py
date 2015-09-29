def main():
    file = open("p79_keylog.txt", "r")
    keys = []
    freq = {}
    for i in file.readlines():
        i = int(i)
        keys.append(i)
        for j in str(i):
            j = int(j)
            if not(j in freq):
                freq[j] = 0
            freq[j] = freq[j] + 1
#    print(keys)
#    print(freq)
    l = []
    while len(l) != 8:
        m = 0
        for i in freq.keys():
            if freq[i] > m and not(i in l):
                m = freq[i]
                m_v = i
        l.append(m_v)
    for i in l:
        i = str(i)
        for j in l:
            j = str(j)
            if j != i:
                for k in keys:
                    k = str(k)
                    if i in k and j in k:
                        if k.index(i) > k.index(j):
                            print(j, i)
                            break
                        else:
                            print(i, j)
                            break
main()
