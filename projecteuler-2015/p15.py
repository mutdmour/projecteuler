def fac(x):
    x_f = 1
 #   l = set()
    for i in range(1,x+1):
        x_f = x_f * i
#        l.add(i)
#    print(l)
    return x_f

def main():

    k = 20
    n = 40

    ans = fac(n) / (fac(k)*(fac(n-k)))

    print(ans)

main()

