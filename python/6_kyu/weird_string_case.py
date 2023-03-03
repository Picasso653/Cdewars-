def to_weird_case(words):
    res = []
    for k in words.split(' '):
        a = odd_even(k)
        res.append(a)
    return ' '.join(res)
def odd_even(word):
    j = ''
    for i in range(len(word)):
        if i%2==0:
            j += word[i].upper()
        else:
            j += word[i].lower()
    return j