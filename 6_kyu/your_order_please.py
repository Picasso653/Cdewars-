def order(sentence):
    if sentence == '':
        return ""
    import re
    x = []
    words = sentence.split(" ")
    for i in words:
        num = re.search(r'\d+', i)
        a = (int(num.group()), i)
        x.append(a)
    x.sort()
    return " ".join([k for j,k in x])