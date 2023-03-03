def to_imparfait(verb_phrase):
    two_words = verb_phrase.split()
    pronoun = two_words[0]
    verb = two_words[-1]
    if pronoun == 'Je' or pronoun == 'Tu':
        return pronoun + ' ' + verb[:-2] + 'ais'
    elif pronoun == "Elle" or pronoun == "Il" or pronoun == 'On':
        return pronoun + ' ' + verb[:-2] + 'ait'
    elif pronoun == "Nous":
        return pronoun +" "+ verb[:-2] + 'ions'
    elif pronoun == "Vous":
        return pronoun +' '+ verb[:-2] + 'iez'
    elif pronoun == "Ils" or "Elles":
        return pronoun +" "+ verb[:-2] + 'aient'