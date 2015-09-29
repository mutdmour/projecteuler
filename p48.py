def main():
    tot = 0
    for i in range(1,1001):
        tot = tot + i**i
    tot = str(tot)
    print((tot)[len(tot)-10:len(tot)])
main()
