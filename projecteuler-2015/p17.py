def define(n):
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fifteen", "eighteen"]
    tens = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    if len(n) == 1:
        if int(n) > 0 and int(n) <10:
            phrase = ones[int(n)]
    elif len(n) == 2:
        if n[0] == "0":
            phrase = define(n[1])
        elif n[0] == "1":
            if int(n) >= 10 and int(n) < 14:
                phrase = ones[int(n)]
            elif int(n) == 15:
                phrase = ones[14]
            elif int(n) == 18:
                phrase = ones[15]
            else:
                phrase = ones[int(n[1])] + "teen"
        elif int(n) % 10 == 0:
            phrase = tens[int(int(n)/10)]
        else:
            phrase = "{0}-{1}".format(tens[int(n[0])], ones[int(n[1])])
    elif len(n) == 3:
        if int(n) % 100 == 0:
            phrase = ones[int(n[0])] + " hundred"
        else:
            phrase = ones[int(n[0])] + " hundred and " + define(n[1:3])
    else:
        phrase = "one thousand"
    
                          
        
 #   print(phrase)
    return(phrase)

def count(n):
    if (" " in n):
        n = n.replace(" ", "")

    if ("-" in n):
        n = n.replace("-", "")
 #       print("yo")
#    print(n)
    return len(n)

def main():
    total = 0
    for i in range(1, 1001):
        x = (define(str(i)))
 #       print(x)
        total = total + count(x)
    print(total)
        
main()
