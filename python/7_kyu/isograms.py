def is_isogram(string):
    the_word = string.lower()
    same= []
    for i in the_word:
        if i in same:
            return False
        else:
            same.append(i)
    return True