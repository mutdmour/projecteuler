def sumList(nums):
    sumList=0
    for i in range(len(nums)):
        sumList=nums[i] + sumList
    return sumList

l = []
for i in range(1000):
    t3 = i / 3
    if t3 == int(t3) or i%5==0:
        l.append(i)
print(sumList(l))
        
