def is_uppercase(inp):
    import re
    regex = r'^[^a-zA-Z]+$'
    if re.match(regex, inp):
        return True
    return inp.isupper()