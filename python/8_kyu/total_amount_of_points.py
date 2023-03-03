def points(games):
    points = 0
    for i in games:
        x = i[0]
        y = i[-1]
        if int(x) > int(y):
            points += 3
        elif int(x) == int(y):
            points += 1
        else:
            points += 0
    return points