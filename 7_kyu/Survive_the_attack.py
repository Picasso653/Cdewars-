def is_defended(attackers, defenders):
    attack_power = sum(attackers)
    defend_power = sum(defenders)
    attack_survivors = 0
    defend_survivors = 0
    attack_army = len(attackers)
    defend_army = len(defenders)
    if attack_army > defend_army:
        diff = attack_army - defend_army
        attack_survivors += diff
        for i in range(defend_army):
            if attackers[i] > defenders[i]:
                attack_survivors += 1
            elif attackers[i] < defenders[i]:
                defend_survivors += 1
    elif defend_army > attack_army:
        diff = defend_army - attack_army
        defend_survivors += diff
        for i in range(attack_army):
            if attackers[i] > defenders[i]:
                attack_survivors += 1
            elif attackers[i] < defenders[i]:
                defend_survivors += 1
    else:
        for i in range(attack_army):
            if attackers[i] > defenders[i]:
                attack_survivors += 1
            elif attackers[i] < defenders[i]:
                defend_survivors += 1
    if attack_survivors == defend_survivors:
        return defend_power >= attack_power
    else:
        return defend_survivors >= attack_survivors