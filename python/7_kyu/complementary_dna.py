def DNA_strand(dna):
    new_dna = ""
    for i in dna:
        if i == "A":
            new_dna += "T"
        elif i == "T":
            new_dna +="A"
        elif i == "G":
            new_dna += "C"
        elif i == "C":
            new_dna += "G"
    return new_dna
        