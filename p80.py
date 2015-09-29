from decimal import *
from math import sqrt

def main():
    getcontext().prec = 102
    tot = 0
    for i in range(2,100):
        k = Decimal(i).sqrt()
        if int(k) != k:
#            k = str(k)
 #           print(k[0:10])
            k = str(k)[0] + str(k)[2:]#[2:]
 #           print(k)
#            print(k[0:10])

            for j in range(100):
                
                tot = tot + int(k[j])
    print(tot)
main()

