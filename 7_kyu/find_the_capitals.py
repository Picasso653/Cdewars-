def capitals(word):
    import string
    return [i for i,j in enumerate(list(word)) if j in list(string.ascii_uppercase)]