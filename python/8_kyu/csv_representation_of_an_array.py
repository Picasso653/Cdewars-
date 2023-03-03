def to_csv_text(array):
    row_strings = []
    for i in array:
        row_strings.append(','.join([str(x) for x in i]))
    return '\n'.join(row_strings)