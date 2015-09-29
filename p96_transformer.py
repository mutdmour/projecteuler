def main():
    file = open('p96_sudoku.txt', 'r')
    outfile = open('p96_sudoku_modified.txt', 'w')
    for i in file.readlines():
 #       print(i)
        if i[0] == 'G':
            print('',file=outfile)
        else:
            s = ''
            for j in i:
                s = s + j + ' '
            print(s, file=outfile)

    outfile.close()
    file.close()

main()
