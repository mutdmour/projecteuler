def main():
    counter = 0
#    counter1 = 0
    for i in range(1, 10000000):
        while i != 1 and i != 89:
            total = 0
            i = str(i)
 #           print(i)
            for j in i:
                total = total + int(j)**2
            i = total
 #       print(i)
        if i == 89:
            counter = counter + 1
        if counter % 100000 == 0:
            print(counter)
#        if i == 1:
#            counter1 = counter1 + 1
    print(counter) #+ counter1)
main()
