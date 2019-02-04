def num(w):
    dic = {'j': 10, 'k': 11, 'h': 8, 'i': 9, 'n': 14, 'o': 15, 'l': 12, 'm': 13, 'b': 2, 'c': 3, 'a': 1, 'f': 6, 'g': 7, 'd': 4, 'e': 5, 'z': 26, 'x': 24, 'y': 25, 'r': 18, 's': 19, 'p': 16, 'q': 17, 'v': 22, 'w': 23, 't': 20, 'u': 21}
    tot = 0
    for i in w:
        tot = tot + dic[i]
    return (tot)


def main():
    file = open("p42_words.txt", "r")
    text = file.read()
    l = set()
    s = ""
    for i in text:
        if i == "\"":
            pass
        elif i == ",":
            l.add(s)
            s = ""
        else:
            s = s + i
    tr = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
    c=0
    for w in l:
        n = num(w.lower())
        while tr[len(tr)-1] < n:
            x = len(tr)+1
            tr.append((1/2)*x*(x+1))
        if n in tr:
            c = c + 1
    print(c)

#num("sky")
main()
