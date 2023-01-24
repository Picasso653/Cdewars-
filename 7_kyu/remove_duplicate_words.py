def remove_duplicate_words(s):
    s = s.split(' ')
    x = []
    for i in s:
        if i not in x:
            x.append(i)
    return ' '.join(x)