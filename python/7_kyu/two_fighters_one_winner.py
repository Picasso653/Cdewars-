def declare_winner(fighter1, fighter2, first_attacker):
    if first_attacker == fighter1.name:
        while fighter1.health >0:
            fighter2.health -= fighter1.damage_per_attack
            if fighter2.health < 0:
                return fighter1.name
            else:
                fighter1.health -= fighter2.damage_per_attack
        return fighter2.name
    else:
         while fighter2.health >0:
            fighter1.health -= fighter2.damage_per_attack
            if fighter1.health < 0:
                return fighter2.name
            else:
                fighter2.health -= fighter1.damage_per_attack
    return fighter1.name