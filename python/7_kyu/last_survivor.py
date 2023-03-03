def last_survivor(letters, coords):
    new_letters = list(letters)
    for pos in coords:
        new_letters.pop(pos)            

    return ''.join(new_letters)