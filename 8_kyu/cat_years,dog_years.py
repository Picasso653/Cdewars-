def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    i = 1
    while i <= human_years:
        if i == 1:
            cat_years += 15
            dog_years += 15
        if i == 2:
            cat_years += 9
            dog_years += 9
        if i > 2:
            cat_years += 4
            dog_years +=5
        i += 1
    return [human_years,cat_years,dog_years]