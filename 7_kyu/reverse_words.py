def reverse_words(text):
    word = text.split(' ')
    reverse = []
    for i in word:
        reverse.append(i[::-1])
    return ' '.join(reverse)