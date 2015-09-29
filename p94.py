from math import sqrt

def area(a,b):
    p = (a*2+b)/2
    A = sqrt(p*(p-a)**2 *(p-b))
    if A % 12 == 0:
        if int(A) == A:
    #           print(a,b,A, a*2+b)
            return a*2+b
    return 0

def main():
    tot = 0
#    m = 0
    for a in range(2, 1000000000):
        b = a - 1
        c = a + 1
        if a*2+b > 1000000000:
            break
        tot = tot + area(a,b) + area(a,c)
 #       if tot > m:
#            print(tot)
#            m = tot
    print(tot)

import time
st = time.time()
main()
end = time.time()
print(end-st)
#print(area(5,6))
