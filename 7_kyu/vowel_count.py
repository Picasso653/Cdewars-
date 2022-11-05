def get_count(sentence):
    vowel_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in sentence:
        if i in vowels:
            vowel_count += 1
    return vowel_count