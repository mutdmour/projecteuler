def main():
    c = 0
    for i in range(1,30):
        for j in range(1,30):
            v = j**i
            if len(str(v)) == i:
                #print(i)
                c = c + 1
    print(c)

main()
