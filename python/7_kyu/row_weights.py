def row_weights(array):
    team1 = []
    team2 = []
    for i in range(len(array)):
        if i%2!=0:  team1.append(array[i])
        else:   team2.append(array[i])
    return (sum(team2),sum(team1))