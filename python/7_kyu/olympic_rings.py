def olympic_ring(string):
    ring_letters = ['a', 'e', 'o', 'p', 'q','P','D', 'b', 'R', 'A', 'o', 'O', 'g', 'Q', 'd']
    one_point = 0
    two_points =0
    two = "B"
    for i in string:
        if  i in two:
            two_points += 2
    for i in string:
        if i in ring_letters:
            one_point += 1
    olympic_points = one_point + two_points
    olympic_medal = int(olympic_points / 2)
    if olympic_medal <= 1:
        return "Not even a medal!"
    elif olympic_medal == 2:
        return "Bronze!"
    elif olympic_medal == 3:
        return "Silver!"
    elif olympic_medal >= 4:
        return "Gold!"
    