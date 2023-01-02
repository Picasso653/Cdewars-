def evaporator(content, evap_per_day, threshold):
    days = 0
    limit = (content*threshold/100)
    while content > limit:
        content -= (content*evap_per_day/100)
        days +=1
    return days