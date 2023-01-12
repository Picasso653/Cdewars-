def rental_car_cost(d):
    if d>2 and d<7:
        return (40*d)-20
    if d>6:
        return (40*d)-50
    return (d*40)