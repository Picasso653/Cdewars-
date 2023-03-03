def square_digits(num):
    string_form = str(num)
    num_output = ''
    my_list = [int(i) for i in string_form]
    for x in my_list:
        square = (x**2)
        num_output += str(square)
    return int(num_output)