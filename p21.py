def factors(n):
#    http://www.stealthcopter.com/blog/2009/11/python-factors-of-a-number/
    from math import sqrt
    fact=[1,n]
    check=2
    rootn= sqrt(n)
    while check<rootn:
            if n%check==0:
                    fact.append(check)
                    fact.append(n/check)
            
            check = check + 1
            print(check)
    if rootn==check:
            fact.append(check)
            fact.sort()
    print(fact)
    return fact



def sumList(nums):
    sumList=0
    for i in range(len(nums)):
        sumList=nums[i] + sumList
    return sumList

def main():
    l = []
    for i in range(0,10000):
        if not(i in l):
            f = factors(i)
 #           print(f)
            a = sumList(f) - i
#            print(a)
    #        print(i, a, f)
            g = factors(a)
            b = sumList(g) - a
    #        print(a, b, g)
 #           if i % 1000 == 0:
#                print(i)
            if a != i and i == b and not(i in l):
                l.append(i)
                l.append(a)
    print(l)
    print(sumList(l))

        
        
factors(10000)
