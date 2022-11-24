def fuel_price(litres, price_per_litre):
    total_price = (price_per_litre*litres)
    if litres >= 2 and litres<4:
        total_price -= (litres*0.05)
    elif litres>= 4 and litres<6:
        total_price -= (litres*0.10)
    elif litres>=6 and litres<8:
        total_price -= (litres*0.15)
    elif litres>=8 and litres<10:
        total_price -= (litres*0.20)
    elif litres>=10:
        total_price -= (litres*0.25)
    return total_price