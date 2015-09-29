def string_rev(s):
    rev = ""
    for i in s:
        rev =  i + rev
    return rev

def palin(s):
    s_n = ""
    for i in s:
        s_n = i + s_n
    if s_n == s:
        return True
    else:
        return False

def main():
    n = 0
    for i in range(10000):
        c = 0
        r = str(i)
        while c < 50:
            r = int(r) + int(string_rev(str(r)))
#            print(r)
            c = c+1
            if palin(str(r)) == True:
                break
        if c == 50:
            n = n + 1

    print(n)

#print(palin("ab"))
main()
