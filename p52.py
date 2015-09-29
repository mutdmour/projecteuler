def string_sort(s):
    l = []
    for m in str(s):
        l.append(m)
    l.sort()
    k = ""
    for m in l:
        k = k + m
    return k

def main():
    for i in range(1,1000000):
        i_s = string_sort(i)
        z = False
        for j in range(2,7):
            k = i * j
            if string_sort(k) != i_s:
                z = False
                break
            z = True
        if z == True:
            print(i)
            break

main()
            
