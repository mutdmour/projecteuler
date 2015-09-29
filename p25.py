def main():
    a=0
    b=1
    counter = 1
    c = 0
    while len(str(c)) < 1000:
        counter = counter + 1
        c=a+b
        b , a = c , b
 #       print(c, len(str(c)), counter)
    print(counter)
main()
