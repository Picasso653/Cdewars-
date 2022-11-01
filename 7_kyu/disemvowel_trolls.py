def disemvowel(string_):
    vowels = ['a','e', 'i', 'o','u', 'A', 'E', 'I', 'O','U']
    no_vowels = ""
    for i in string_:
        if i not in vowels:
            no_vowels += i
    return no_vowels