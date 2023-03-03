def no_odds(values):
    if values != []:
        return [i for i in values if i%2 == 0]
    return []