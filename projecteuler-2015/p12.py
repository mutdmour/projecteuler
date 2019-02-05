#http://projecteuler.net/problem=12
#What is the value of the first triangle number to have over five hundred divisors?

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
#            print(check)
    if rootn==check:
            fact.append(check)
            fact.sort()
 #           print(check)
#    print(fact)
    return len(fact)

def factors_me(n):
    from math import sqrt
    fact = [1,n]
    rootn = sqrt(n)
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            fact.append(i)
            if not(n/i in fact):
                fact.append(n/i)
    fact.sort()
    print(fact)
#    return len(fact)
            
            

def main():
    c = 1
    a = 0
    n = 0
    while n < 500: #this repeats until the number of factors is equal to 500
        a = a + c
        c = c + 1 #this is the counter, incrementing by one
        n = factors_me(a)
    print(a)
                
#main()

factors(36)
