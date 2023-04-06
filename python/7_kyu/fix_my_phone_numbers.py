def is_it_a_num(s: str) -> str:
    num = ''
    for i in s:
        if i.isnumeric():
            num += i
    if num == '':
        return "Not a phone number"
    elif num[0] != '0' or len(num) != 11:
        return "Not a phone number"
    else: return num