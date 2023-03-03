def mango(quantity, price):
    return sum([price for i in range(quantity+1) if i%3!=0])