def main():
 #   s = "0123456789"
#    l = "9876543210"
    counter = 0
    for i in range(123456789, 9876543211):
        i = str(i)
        if len(i) == 9:
            i = "0" + i
 #       print(i)
        if ("0" in i) and ("1" in i) and ("2" in i) and ("3" in i) and ("4" in i) and ("5" in i) and ("6" in i) and ("7" in i) and ("8" in i) and ("9" in i):
#            print("yo")
            counter = counter + 1
            if counter % 1000 == 0:
                print(counter)
            if counter == 1000000:
                print(i)
                break
main()
