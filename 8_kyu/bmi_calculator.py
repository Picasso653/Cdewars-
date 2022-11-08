def bmi(weight, height):
    bmi_calc = weight / (height ** 2)
    if  bmi_calc <= 18.5:
        return "Underweight"
    elif bmi_calc <= 25.0:
        return "Normal"
    elif bmi_calc <= 30.0:
        return "Overweight"
    elif bmi_calc > 30:
        return "Obese"