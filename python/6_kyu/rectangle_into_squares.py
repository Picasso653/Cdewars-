def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None
    area = lng * wdth
    result = []
    while lng > 0 and wdth > 0:
            if lng > wdth:
                result.append(wdth)
                lng -= wdth
            else:
                result.append(lng)
                wdth -= lng
    return result