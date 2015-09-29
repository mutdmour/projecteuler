def main():
    tri = [0]
    v = 1
    n = 0
    while len(str(v)) < 5:
        n = 1 + n
        v = int(n * (n+1)/2)
 #       print(n,v)
        if len(str(v)) == 4:
            tri.append(v)
        else:
            tri.append(0)
            
    sq = [0]           
    v = 1
    n = 0
    while len(str(v)) < 5:
        n = 1 + n
        v = int(n**2)
 #       print(n,v)
        if len(str(v)) == 4:
            sq.append(v)
        else:
            sq.append(0)
 #   print(sq)

    pent = [0]           
    v = 1
    n = 0
    while len(str(v)) < 5:
        n = 1 + n
        v = int(n*(3*n-1)/2)
 #       print(n,v)
        if len(str(v)) == 4:
            pent.append(v)
        else:
            pent.append(0)

 #   print(pent)

    hexa = [0]           
    v = 1
    n = 0
    while len(str(v)) < 5:
        n = 1 + n
        v = int(n*(2*n-1))
 #       print(n,v)
        if len(str(v)) == 4:
            hexa.append(v)
        else:
            hexa.append(0)

 #   print(hexa)

    hept = [0]           
    v = 1
    n = 0
    while len(str(v)) < 5:
        n = 1 + n
        v = int(n*(5*n-3)/2)
 #       print(n,v)
        if len(str(v)) == 4:
            hept.append(v)
        else:
            hept.append(0)

#    print(hept)     


    octa = [0]           
    v = 1
    n = 0
    while len(str(v)) < 5:
        n = 1 + n
        v = int(n*(3*n-2))
   #     print(n,v)
        if len(str(v)) == 4:
            octa.append(v)
        else:
            octa.append(0)

#    tri = [8128]
#    sq = [0, 2881]
#    pent = [0, 0, 8143,8170]
#    hexa = [0, 0, 0, 4315, 6211]
#    hept = [0, 0, 0, 0, 1570, 0,1181]
#    octa = [0, 0, 0, 0, 0, 7062]

    p = [sq, pent, hexa, hept, octa]

     
    for i in range(len(tri)):
         if tri[i] != 0:
               ans = []
               pos = []
               v = []
               ans.append(tri[i])
               pos.append(i)
               v.append('t')
               find_next(ans, v, pos, p)
               if len(ans) == 6:
#                    print(ans)
 #                   print(v)
#                    print(pos)
                    break
    tot = 0
    for i in ans:
          tot = tot + i
    print(tot)
               
def find_next(ans, v, pos, p):
 #    print(ans)
     if len(ans) == 6:
          if str(ans[0])[0:2] == str(ans[len(ans)-1])[2:4]:
               return
          else:
               ans.pop(len(ans)-1)
               pos.pop(len(pos)-1)
               v.pop(len(v)-1)
               return
     c = -1
     for l in p:
          c = c + 1
          if not (c in v):
               for i in range(len(l)):
                    if not(i in pos):
                      a = str(l[i])[0:2]
                      b = str(l[i])[2:4]
                      k = str(ans[len(ans)-1])[2:4]
                      if a == k:
                           ans.append(l[i])
                           pos.append(i)
                           v.append(c)
                           find_next(ans, v, pos, p)
                           if len(ans) == 6:
                                return
     ans.pop(len(ans)-1)
     pos.pop(len(pos)-1)
     v.pop(len(v)-1)
     return
     
                                                 
main()
