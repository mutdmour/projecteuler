def main():
    file = open("p8_input.txt", "r")
    s = ""
    for i in file.readlines():
        s = s + i[0:-1]

    i = 0
    m = 0
    while i != 995:
        p = int(s[i]) * int(s[i+1]) * int(s[i+2]) * int(s[i+3]) * int(s[i+4])
        if p > m:
            m = p
        i = i + 1

    print(m)
main()
