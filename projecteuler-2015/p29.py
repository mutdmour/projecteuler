def main():
    ans = []
    for a in range(2,101):
        for b in range(2,101):
            y = a**b
            if not(y in ans):
                ans.append(y)

    print(len(ans))

main()
