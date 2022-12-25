def duplicate_encode(word):
    parenthesis = ''
    for i in word.lower():
        if word.lower().count(i) == 1:
            parenthesis += "("
        else:
            parenthesis += ")"
    return parenthesis