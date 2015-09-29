def main():
    from math import floor
    tot = 0
    for n in range(10**20):
        n = str(n)
        par = 0
        for i in n:
            i = int(i)
            par = par + i**2
 #       print(n,par)
        if (par)**(1/2) == floor(par**(1/2)):
            tot = tot + int(n)
 #           print(n, par)
    tot = str(tot)
    ha = tot[len(tot)-9:len(tot)]
    print(ha)
main()
