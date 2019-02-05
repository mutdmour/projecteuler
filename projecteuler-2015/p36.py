def binary(n):
    v = [2**0]
    b = []
    if n == 0:
        return "0"
    while n>=v[len(v)-1]:
        v.append(2**len(v))
    v.reverse()
    for i in v:
        if n < i:
            b.append(0)
        else:
            n = n - i
            b.append(1)
    while b[0] == 0:
        b.pop(0)
    s = ""
    for i in b:
        s = s + str(i)
    return (s)

def palin(s):
    s_n = ""
    for i in s:
        s_n = i + s_n
    if s_n == s:
        return True
    else:
        return False


def main():
    tot = 0
    for i in range(0,1000000):
        b = binary(i)
        s = str(i)
        if palin(s) ==True and palin(b)==True:
            tot = tot + i
 #           print(i,b)
    print(tot)

main()
