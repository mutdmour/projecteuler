def main():
    file = open("p22_names.txt", "r")
    line = file.readline()
    for i in line:
        line = line.replace("\",\"", " ")
        line = line.replace("\"", "")
#    print(line)
    names = line.split()
    names.sort()
    position = 1
    total_score = 0
 #   print(names)
 #   names = ['COLIN']
    for i in names:
        total = 0
        for j in i:
            total = total + ord(j) - 64
        score = position * total
        if i == 'COLIN':
            print(position, total, score)
        position += 1
        total_score = total_score + score
    print(total_score)
    
main()
