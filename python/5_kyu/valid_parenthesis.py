def valid_parentheses(string):
    bracket = []
    for i in string:
        if i =="(" or i ==")":
            bracket.append(i)
    if ''.join(bracket) == '':
        return True
    if bracket[0]==")" or bracket[-1]== "(":
        return False
    if len(bracket) %2==0:
        x = 0
        for i in bracket:
            if i == "(":
                x +=1
            else:
                x -=1
            if x <0:
                return False
        if x==0:
            return True
            
    return False
