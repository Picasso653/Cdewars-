def create_phone_number(n):
    s = ''.join([str(i) for i in n])
    a = s[0:3]
    b = s[3:6]
    c = s[6:]
    return f"({a}) {b}-{c}"