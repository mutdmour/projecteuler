def main():
    file = open("p13_input.txt", "r")
    total = 0
    for i in file.readlines():
        total = total + int(i)
    total = str(total)
    print(total[0:9])
main()
