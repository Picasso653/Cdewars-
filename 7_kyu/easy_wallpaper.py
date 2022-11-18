def wallpaper(l, w, h):
    numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"]
    formula1 = 2 * (h*w) + 2 * (l*h)
    formula2 = formula1 / 5.2
    formula3 = 0.15 * formula2
    last_formula = formula3 + formula2
    final_form = int(last_formula)
    if l == 0 or w == 0 or h == 0:
        return "zero"
    else:
        return numbers[final_form +1]
    