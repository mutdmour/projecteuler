def main():
    m = 0
    for D in range(1,101):
 #       print(D)
        k = D**(1/2)
        if k != int(k):
            x = .1
            y = 0
            while int(x) != x:
                y = y+1
                x = (1+D*y**2)**(1/2)
#                print(D, y,x, y/x)
            print(x, D, y)
            if x > m:
                m = x
                v = D
 #               print(m)
    print(v)

main()

#not working
