def Position(letter,string):
    letter_list = letter.split(" ")
    index=[]
    x = -1
    check = 0
    for i in letter_list:
        x+=1
        if string in i:
            index.append(x)
            y=0
            for j in i:
                y+=1
                if j == string:
                    index.append(y)
        else:
            check+=1
            if check == len(letter_list):
                index.append(-1)
            continue
    return index
print(Position("pythone is simple language","p"))