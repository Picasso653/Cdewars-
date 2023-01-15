def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    import math
    square_list = [age_1**2, age_2**2, age_3**2, age_4**2,age_5**2,age_6**2,age_7**2,age_8**2]
    x = sum(square_list)
    y = math.sqrt(x)
    return int(y/2)
