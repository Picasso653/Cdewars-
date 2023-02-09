def is_valid_IP(strng):
    if strng == '': return False
    print(strng)
    if '.' not in strng: return False
    if ' ' in strng: return False
    for i in strng.split('.'):
        if not is_integer(i):   return False
        if i[0] == '0' and len(i)>1: return False
        if int(i)<0: return False
        if int(i)>255: return False
    return len(strng.split('.'))==4


def is_integer(x):
    try:
        int(x)
        return True
    except ValueError:
        return False