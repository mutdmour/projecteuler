def main():
    c = 0
    for i in range(12, 1000):
        n = 0
        l = set()
        z = True
        for h in range(1,i):
            for w in range(1,i):
 #               print(i, h, w, h+w)
                if (h + w) < i:
 #                   print("hey")
                    if (h**2 + w**2) == (i-h-w)**2 and not(w in l):
#                        print(i, h,w,i-h-w)
                        n = n + 1
                        l.add(h)
      #                  print(l)
                    if n > 1:
                        z = False
                        break
                else:
                    break
            if z == False:
#                print("yo")
                break
        if n == 1:
            c = c + 1
#            print(i)
    print(c)

main()
