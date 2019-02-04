def odd(n):
    t = 3 * n + 1
    return t

def even(n):
    t = n / 2
    return t

def collatz(n):
            l = []
            l.append(n)
            while n != 1:
                t = n / 2
                if t == int(t):
                    n = even(n)
                    l.append(n)
                else:
                    n = odd(n)
                    l.append(n)
            return len(l)

def main():
    m=0
    for i in range(10**6, 1, -1):
        t = collatz (i)
        if m < t:
            n = i
            m = t
    print(n, m)

main()
