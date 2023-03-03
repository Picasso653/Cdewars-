def to_camel_case(text):
    import re
    list = re.split(r"[_-]", text)
    res = [list[0]]
    for i in list[1:]:
        res.append(i.capitalize())
    return ''.join(res)