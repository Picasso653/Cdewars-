def year_days(year):
    pos_year = abs(year)
    if year%100==0 and year%400!=0:
        return "{y} has 365 days".format(y = year)
    elif pos_year%4==0 or (pos_year%100==0 and pos_year%400==0):
        return "{y} has 366 days".format(y = year)
    else:
        return "{y} has 365 days".format(y = year)
    