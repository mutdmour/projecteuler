def sumvalues(n):
    s = str(n)
    total = 0
    for i in range(len(s)):
        total = total + int(s[i])
    return total
        

def main():
    z = False
    j = 20
    while z == False:
#        if sumvalues(j)%3 == 0: #this does not make it faster
            for i in [7,11,13,16,17,18,19,20]:
                if j % i == 0:
                    c = True
                    pass
                else:
                    c = False
                    break
            if c == True:
                print(j)
                break
            j = j + 10 #made it faster by realizing that the last digit has to be a zero

main()
