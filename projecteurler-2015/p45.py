def main():
    P = set()
    H = set()
    ans = []
    for i in range(1,100000):
        t = i*(i+1)/2
        p = i*(3*i-1)/2
        h = i*(2*i-1)
        P.add(p)
        H.add(h)
        if (t in P) and (t in H):
            ans.append(t)
    print(ans)

main()
