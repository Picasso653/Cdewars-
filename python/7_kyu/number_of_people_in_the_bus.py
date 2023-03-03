def number(bus_stops):
    first_lift = bus_stops[0]
    x = first_lift[0]
    bus_stops.remove(bus_stops[0])
    for i in bus_stops:
        x += i[0]
        x -= i[-1]
    return x