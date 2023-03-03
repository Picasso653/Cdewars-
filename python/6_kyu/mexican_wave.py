def wave(people):
    if people == '':
        return []
    the_wave = []
    for i in range(len(people)):
        if people[i].isalpha():
            a = people[:i]+people[i].upper()+people[i+1:]
            the_wave.append(a)
    return the_wave