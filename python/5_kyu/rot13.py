def rot13(message):
    rot_letters = "abcdefghijklmnopqrstuvwxyz"
    res = ''
    for i in message:
        if i.isalpha():
            a = rot_letters.index(i.lower())
            b = a+13
            c = b%26
            if i.isupper(): res += rot_letters[c].upper()
            else:   res += rot_letters[c]
        else: res += i
    return res