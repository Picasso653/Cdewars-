def ordered_count(inp):
    actual_count =[]
    for letter in inp:
        num = inp.count(letter)
        group = (letter, num)
        actual_count.append(group)
    return list(dict.fromkeys(actual_count))