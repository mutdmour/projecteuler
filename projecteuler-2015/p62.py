def comp(a,b):
    if len(str(a)) == len(str(b)):
        for i in str(a):
            if str(b).count(i) != str(a).count(i):
                return False
        return True
    return False

def main():
    n = 5
    i = -1
    cubes = []
    ans = []
    while len(ans) != n and i < 10000:
        z = False
        i = i + 1
        if i == 8384:
            z = True
        v = i**3
        ans = [i]
        for j in range(len(cubes)-1, 0, -1):
            if len(str(cubes[j])) < len(str(v)):
                break
            elif comp(v, cubes[j]):
#                if z == True:
#                    print(v, cubes[j])
 #               print(v, cubes[j])
                ans.append(j)
        cubes.append(v)
        z = False
    print(v)
    
import time
st = time.time()
main()
end = time.time()
print(end-st)
#print(comp(5027**3, 7061**3))
