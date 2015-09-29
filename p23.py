def factor(n):
    factors = [n, 1]
    for i in range(2, int(n**(1/2))+1):
        if n % i == 0:
            factors.append(i)
            if not (n/i in factors):
                factors.append(n/i)
    factors.sort()
#    print(factors)
    return factors

def sumList(nums):
    sumList=0
    for i in range(len(nums)):
        sumList=nums[i] + sumList
    return sumList

def abundant():
    abundant = []
    n = 12
    outfile = open("p23_abundant.txt", "w")
#    abundant_counter = 0
#    perfect_counter = 0
#    dificient_counter = 0
    while n >= 12 and n <= 28123:
        factors = factor(n)
        total = sumList(factors) - n
        if total > n:
            print(n, file=outfile)
 #           abundant.append(n)
#            abundant_counter = abundant_counter + 1
#        elif total == n:
#            perfect_counter = perfect_counter +1
#            print(n)
#        else:
#            dificient_counter = dificient_counter +1
        n = n+1
        
#def main():
#    l = []
#    abundant = []
#    file = open("p23_abundant.txt", "r")
#    for i in file.readlines():
#        abundant.append(int(i[0:len(i)-1]))
 #   print(abundant)
#    for i in range(24, 28124):
#         for j in abundant:
#             if i > j:
#                 t = i - j
#                 print(i, j, t)
#                 if (t in abundant) == True:
#                     print("yo")
#                     z = False
#                     break
#                 else:
#                     z = True
     #                print("yo")
#         if z == True:
#             l.append(i)
#    answer = sumList(l)
#    print(answer)

def checkabundant(n):
    factors = factor(n)
    total = sumList(factors) - n
    if total > n:
        return True
    else:
        return False


def main():
    abundant = []
#    answer = []
    total = 0
    for i in range(24, 100):
        for j in range(12, i, 2):                
                if not(j in abundant):
                    x = checkabundant(j)
                else:
                    x = True
 #               print(j, x)
                if x == True:
                    abundant.append(j)
                    t = i - j
                    if not(t in abundant):
                        c = checkabundant(t)
                    else:
                        c = True
                    if c == True:
                        abundant.append(t)
                        z = False
                        break
                    else:
                        z = True
 #               else:
#                    z = False
#                print(i, j, x, t, c)
        if i % 100 == 0:
            print(i)
        if z == True:
 #           print("yo")
            total = total + i
    total = total + 273 #the 273 is for the sum of numbers from 1 till 23
    print(total)
#            answer.append(i)
 #   print((abundant) , (not_abundant))


main()
