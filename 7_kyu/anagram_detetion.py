def is_anagram(test, original):
    n = 0
    for i in test.lower():
        if i in list(original.lower()):
            n +=1
    return n == len(original) and n == len(test)