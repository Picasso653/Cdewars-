def pig_it(text):
    res = []
    piglet = text.split(" ")
    for i in piglet:
        if i.isalpha():
            piggay = i[1:]+i[0]+"ay"
            res.append(piggay)
        else:
            res.append(i)
    return " ".join(res)