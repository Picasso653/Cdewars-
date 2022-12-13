def count_squares(cuts):
    x = (2 * (cuts + 1) ** 2) + (cuts - 1) * ((cuts - 1) * 4 + 4)
    return x