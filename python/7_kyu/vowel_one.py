def vowel_one(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_one = ''
    for i in s.lower():
        if i in vowels:
            vowel_one += '1'
        else:
            vowel_one += '0'
    return vowel_one