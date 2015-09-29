def sumList(nums):
    sumList=0
    for i in range(len(nums)):
        sumList=nums[i] + sumList
    return sumList

def checkeven(nlist):
    for i in range(len(nlist)):
        if nlist[i]%2 != 0:
            nlist[i] = 0
        
def main():
    l = []
    a = 0
    b = 1
    c = a + b
    while c < 4000000:
        c=a+b
        l.append(c)
        b , a = c , b
    checkeven(l)
    print(sumList(l))

main()
