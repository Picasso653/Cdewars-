def open_or_senior(data):
    data_list = []
    for list in data:
        if (list[0] >= 55) and (list[-1] in range(8, 27)):
             data_list.append('Senior')
        else:
            data_list.append('Open')
    return data_list