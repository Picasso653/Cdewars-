def solution(n):
    x = len(str(n))
    a = list(str(n).zfill(4))
    complete = thousands(a[0])+hundreds(a[1])+tens(a[2])+ones(a[3])
    return complete
    
def thousands(a):
    v = ''
    v += "M" * int(a)
    return v
def hundreds(a):
    v = ''
    if int(a) == 0: v += ''
    elif int(a) == 4: v += "CD"
    elif int(a) == 5: v += "D"
    elif int(a) >= 6 and int(a)!= 9: v += "D" + ("C"*(int(a)-5))
    elif int(a) == 9: v += "CM"
    else: v += "C" * int(a)
    return v
def tens(a):
    v = ''
    if int(a) == 0: v += ''
    elif int(a) == 4: v += "XL"
    elif int(a) == 5: v += "L"
    elif int(a) >= 6 and int(a)!= 9: v += "L" + ("X"*(int(a)-5))
    elif int(a) == 9: v += "XC"
    else: v += "X" * int(a)
    return v
def ones(a):
    v = ''
    if int(a) == 0: v += ''
    elif int(a) == 4: v += "IV"
    elif int(a) == 5: v += "V"
    elif int(a) >= 6 and int(a)!= 9: v += "V" + ("I"*(int(a)-5))
    elif int(a) == 9: v += "IX"
    else: v += "I" * int(a)
    return v
