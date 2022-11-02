def bar_triang(point_a, point_b, point_c): 
    _add_x = point_a[0] + point_b[0] + point_c[0]
    _add_y = point_a[1] + point_b[1] + point_c[1]
    barry_x = round((_add_x / 3), 4)
    barry_y = round((_add_y/3), 4)
    return [barry_x , barry_y]