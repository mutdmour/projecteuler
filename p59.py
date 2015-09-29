def define(n):
    l = []
    for i in range(0,127):
        for j in range(97,123):
            if j + i > 127:
                k = j + i - 127
            else:
                k = j + i
            if k == n:
                l.append("{0},{1}".format(chr(i),chr(j)))
    return l

def main():
    file = open("p59_cipher1.txt","r")
    text = []
    for  i in file.readlines():
        for j in range(len(i)):
            if i[j] == ",":
                i[j] = " "
            i = i.split()
            for j in range(len(i)):
                i[j] = define(int(i[j]))
            text.apeend(i)

print(define(79))

