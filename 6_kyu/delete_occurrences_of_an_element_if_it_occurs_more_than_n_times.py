def delete_nth(order,max_e):
    result = []
    for i in order:
        if result.count(i) < max_e:
            result.append(i)
    return result