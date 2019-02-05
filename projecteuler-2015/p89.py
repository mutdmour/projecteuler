def read(roman):
    read = []
    for i in roman:
        if i == "I":
            read.append(1)
        elif i == "V":
            read.append(5)
        elif i == "X":
            read.append(10)
        elif i == "L":
            read.append(50)
        elif i == "C":
            read.append(100)
        elif i == "D":
            read.append(500)
        elif i == "M":
            read.append(1000)

#    print(read)
    
    for j in range(len(read)-1):
        if read[j] < read[j+1]:
            read[j] = - read[j]

#    print(read)

    tot = 0
    for i in read:
        tot = tot + i
    return (tot)

def minimal(num):
    roman = ""
    while num >= 1000:
        num = num - 1000
        roman = roman + ("M")
    while num >= 500:
        num = num - 500
        roman = roman + ("D")
    while num >= 100:
        num = num - 100
        roman = roman + ("C")
    while num >= 50:
        num = num - 50
        roman = roman + ("L")
    while num >= 10:
        num = num - 10
        roman = roman + ("X")
    while num >= 5:
        num = num - 5
        roman = roman + ("V")
    while num > 0:
        num = num - 1
        roman = roman + ("I")

    return roman
        
def main():
    tot = 0
    file = open ('p89_roman.txt', 'r')
    for i in file.readlines():
        i = (i[0:-1])
        num = read(i)
        minim = minimal(num)
        print(num)
        print(i)
        print(minim)
        print("")
        k = len(i)
        dif = num - k
        tot = tot + dif
        
