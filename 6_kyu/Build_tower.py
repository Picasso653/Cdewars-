def tower_builder(n_floors):
    m = int(((n_floors*2)-2)/2)
    print(m)
    tower = []
    if n_floors == 1:
        tower.append("*")
    else:
        for i in range(n_floors):
            if i%2==0:
                x = m*' '+i*2*"*"+"*"+m*' '
            else:
                x = m*' '+"*"+(i*2)*"*"+m*' '
            tower.append(x)
            m -= 1
    return tower

print(tower_builder(4))