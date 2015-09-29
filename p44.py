def main():
    pent = [1,5]
    for i in range(3,10000):
        z = False
        tot = (i*(3*i-1)/2)
        for j in pent:            
            k = tot - j
            if (k in pent):
                dif = abs(k - j)
#                print(j, k, tot, dif, dif in pent)
                if dif in pent:
                    print(dif)
                    z = True
                    break
        pent.append(tot)
        if z == True:
 #           print(dif)
            break
main()
