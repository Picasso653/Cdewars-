geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    new_birds = []
    for i in birds:
        if i not in geese:
            new_birds.append(i)
    return new_birds
        