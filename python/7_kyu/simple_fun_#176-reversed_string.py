def reverse_letter(string):
    return ''.join([i for i in string if i.isalpha()][::-1])