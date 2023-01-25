def dirReduc(arr):
    if arr==[]:
        return []
    short_cut = ['dummy_variable',arr[0]]
    for i in arr[1:]:
        if opposite_direction(i) == short_cut[-1]:
            short_cut.pop()
        else: short_cut.append(i)
    x = short_cut[1:]
    return x

def opposite_direction(a):
    forward =['NORTH', 'EAST']
    backward = ['SOUTH', "WEST"]
    if a in forward:
        b = forward.index(a)
        return backward[b]
    else:
        b = backward.index(a)
        return forward[b]