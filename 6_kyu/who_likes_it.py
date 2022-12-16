def likes(names):
    if names == []:
        return "no one likes this"
    if len(names) >= 2 and len(names) < 4:
        return ', '.join(names[0:-1]) + " and " + names[-1] + " like this"
    if len(names) == 1:
        return names[0] + " likes this"
    else:
        return ', '.join(names[0:2]) + " and " + str(len(names) - 2) + " others like this"