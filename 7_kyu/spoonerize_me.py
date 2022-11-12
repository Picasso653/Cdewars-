def spoonerize(words):
    arr = words.split()
    wordx = arr[1]
    wordy = arr[0]
    spooned_word = wordy[0]+ wordx[1:] + " " + wordx[0]+ wordy[1:]
    return spooned_word


