def main():
    ans = set()
    for i in range(2,10000000):
        j = str(i)
        tot = 0
        for k in j:
            tot = tot + int(k)**5
        if tot == i:
            ans.add(i)

    tot = 0
    for i in ans:
        tot = tot + i

    print(tot)

main()
