def define_kind(l): #for a list
    for k in range(len(l)):
        if l[k] == "T":
            l[k] = "10"
        elif l[k] == "J":
            l[k] = "11"
        elif l[k] == "Q":
            l[k] = "12"
        elif l[k] == "K":
            l[k] = "13"
        elif l[k] == "A":
            l[k] = "14"
    return l

def checkRF(h):
    l = []
    for k in h:
        l.append(k[1])
    if len(l) != l.count(l[0]):
        return False
    else:
        l = []
        for k in h:
            l.append(k[0])
        if "T" in l and "J" in l and "Q" in l and "K" in l and "A" in l:
            return True

def checkSF(h):
    l = []
    for k in h:
        l.append(k[1])
    if len(l) != l.count(l[0]):
        return False
    else:
        l = []
        for k in h:
            l.append(k[0])
        l = define_kind(l)
        l.sort()
        i = int(l[0])
        if str(i) in l and str(i+1) in l and str(i+2) in l and str(i+3) in l and str(i+4) in l:
            return True
        else:
            return False

def checkFK(h):
    l = []
    for k in h:
        l.append(k[0])
    l = define_kind(l)
    for i in l:
        c = l.count(i)
        if c == 4:
            return True
        elif c == 3 or c == 2:
            return False
    return False

def checkFH(h): #3 of a kind and a pair
    x, y = checkTK(h)
    r, s = checkOP(h)
    if x == True and r == True:
        return True, y, s
    return False, 0, 0

def checkFl(h):
    l = []
    for k in h:
        l.append(k[1])
    if len(l) != l.count(l[0]):
        return False
    return True

def checkSt(h):
    l = []
    for k in h:
        l.append(k[0])
    l = define_kind(l)
    l.sort()
    i = int(l[0])
    if str(i) in l and str(i+1) in l and str(i+2) in l and str(i+3) in l and str(i+4) in l:
        return True
    else:
        return False

def checkTK(h):
    l = []
    for k in h:
        l.append(k[0])
    l = define_kind(l)
    for i in l:
        c = l.count(i)
        if c == 3:
            return True, i
    return False, 0    

def checkTP(h):
    l = []
    for k in h:
        l.append(k[0])
    l = define_kind(l)
    n = 0
    e = set()
    k = "0"
    for i in l:
        c = l.count(i)
        if c == 2 and not(i in e):
            n = n+1
            e.add(i)
            if i > k:
                k = i
    if n == 2:
        return True, k
    else:
        return False, 0

def checkOP(h):
    l = []
    for k in h:
        l.append(k[0])
    l = define_kind(l)
    for i in l:
        c = l.count(i)
        if c == 2:
            return True, i
    return False, 0

def highest(a,b):
    l_a = []
    l_b = []
    for k in a:
        l_a.append(k[0])
    l_a = define_kind(l_a)

    for k in b:
        l_b.append(k[0])
    l_b = define_kind(l_b)

    for i in range(len(l_a)):
        l_a[i] = int(l_a[i])
    for i in range(len(l_b)):
        l_b[i] = int(l_b[i])
        
    l_a.sort()
    l_b.sort()
    l_a.reverse()
    l_b.reverse()

#    print(l_a, l_b)

    for i in range(5):
        if l_a[i] > l_b[i]:
            return True
        elif l_a[i] < l_b[i]:
            return False
    return False

def comp_FK(a,b):
    l_a = []
    for k in h:
        l_a.append(k[0])
    l_a = define_kind(l_a)
    for i in l_a:
        c = l_a.count(i)
        if c == 4:
            k_a = i

    l_b = []
    for k in h:
        l_a.append(k[0])
    l_b = define_kind(l_b)
    
    for i in l_b:
        c = l_b.count(i)
        if c == 4:
            k_b = i    

    if int(k_a) > int(k_b):
        return True
    else:
        return False

def compare(a,b): #player 1 is True
    if checkRF(a) == True:
        if checkRF(b) == False:
#            print("1 has a royal flush")
            return True
    else:
        if checkRF(b) == True:
#            print("2 has a royal flush, but not 1")
            return False

#    print("neither has a royal flush")
        
    if checkSF(a) == True:
        if checkSF(b) == False:
#            print("p1 has a straight flush")
            return True
        else:
#            print("both have straight flushes, need to choose the highest value")
            return highest(a,b)
    else:
        if checkSF(b) == True:
#            print("p2 has a straight flush")
            return False
        
#    print("no Straight Flush: All cards are consecutive values of same suit.")
          
    if checkFK(a) == True:
        if checkFK(b) == False:
#            print("p1 has a four of a kind")
            return True
        else:
#            print("both have a four of a kind, need to compare the two values")
            return comp_FK(a,b)
    else:
        if checkFK(b) == True:
#            print("p2 has a four of a kind")
            return False
#    print("no four of a kind")
          
    x_a, y_a, z_a = checkFH(a)
    x_b, y_b, z_b = checkFH(b)
    if x_a == True:
        if x_b == False:
#            print("p1 has a full house")
            return True
        else:
#            print("both have a full house, need to compare the cards of three, if same, then the pair")
            if int(y_a) > int(y_b):
                return True
            elif int(y_b) > int(y_a):
                return False
            else:
                if int(z_a) > int(z_b):
                    return True
                else:
                    return False
                    
    else:
        if x_b == True:
#            print("p2 has a full house")
            return False

#    print("no full house: three of a kind and a pair")

    if checkFl(a) == True:
        if checkFl(b) == False:
#            print("p1 has a flush")
            return True
#        else:
#            print("both have a flush, need to see the next in rank, straight")
    else:
        if checkFl(b) == True:
#            print("p2 has a flush")
            return False

#    print("no flush: All cards of the same suit.")

    if checkSt(a) == True:
        if checkSt(b) == False:
#            print("p1 has a straight")
            return True
        else:
#            print("both have a straight, need to choose the highest")
            return highest(a,b)
    else:
        if checkSt(b) == True:
#            print("p2 has a flush")
            return False

#    print("no Straights: All cards are consecutive values.")
            
    x_a, y_a = checkTK(a)
    x_b, y_b = checkTK(b)
    if x_a == True:
        if x_b == False:
#            print("p1 has a three of a kind")
            return True
        else:
#            print("both have a three of a kind, gotta compare their values")
            if int(y_a) > int(y_b):
                return True
            else:
#                print("p2 wins, but hope they are not equal")
                return False
    else:
        if x_b == True:
#            print("p2 has a three of a kind")
            return False
          
#    print("no three of a kinds")
    
    x_a, y_a = checkTP(a)
    x_b, y_b = checkTP(b)
    if x_a == True:
        if x_b == False:
#            print("p1 has two pairs")
            return True
        else:
#            print("both have two pairs, need to compare their values")
            if int(y_a) > int(y_b):
                return True
            elif int(y_a) == int(y_b):
#                print("same values, check highest")
                return highest(a,b)
            else:
                return False
    else:
        if x_b == True:
#            print("p2 has two pairs")
            return False
          
#    print("no two pairs")
          
    x_a, y_a = checkOP(a)
    x_b, y_b = checkOP(b)
    if x_a == True:
        if x_b == False:
#            print("p1 has one pair")
            return True
        else:
#            print("both have two pairs, need to compare values, highest if the same pair")
            if int(y_a) > int(y_b):
                return True
            elif int(y_a) == int(y_b):
                return highest(a,b)
            else:
                return False
    else:
        if x_b == True:
#            print("p2 has one pair, cute")
            return False
#    print("no even one pair")
          
#    print("highest?")
    return highest(a,b)
    

def main():
    file = open("p54_poker.txt", "r")
    c = 0
    for i in file.readlines():
        a = []
        b = i.split()
        for j in range(5):
            a.append(b.pop(0))
#        print(a,b)
        if compare(a,b) == True:
            c = c + 1
#            print("P1 wins")
#        else:
#            print("P2 wins")
#        r = input("next?")
#        print("")
    print(c)
main()
#print(compare(['5D', '8C', '9S', 'JS', 'AC'], ['2C', '5C', '7D', '8S', 'QH']))
#print(checkTK("3C 3D 3S 9S 9D".split()))
#print(define_kind(["T", "K", "Q", "4"]))
