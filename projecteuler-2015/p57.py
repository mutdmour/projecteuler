def main():
    from fractions import Fraction
    c = 0
    n = 0
    v = 1
    for i in range(1,1000):
        v = Fraction(v-1)
        while n != i:
            n = n+1
            v = Fraction(1/(2+v))
        v= Fraction(1 + v)
    #    print(v)
        s = str(v)
        #print(s)
        for i in range(len(s)):
            if s[i] == "/":
                a = i
                b = len(s)-(i+1)
                break
        if a>b:
     #       print(a,b)
            c = c + 1
    print(c)

import time
start = time.time()
main()
end = time.time()
print(end-start)
