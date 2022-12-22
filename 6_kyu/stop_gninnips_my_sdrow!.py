def spin_words(sentence):
    spin = []
    for i in sentence.split(" "):
        if len(i) >= 5:
            spin.append(i[::-1])
        else:
            spin.append(i)
    return ' '.join(spin)