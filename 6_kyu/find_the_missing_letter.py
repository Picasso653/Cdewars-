def find_missing_letter(chars):
    import string
    a = [i for i in string.ascii_lowercase]
    A = [I for I in string.ascii_uppercase]
    if chars[0].isupper():
        num = A.index(chars[0])
        y = 0
        for x in range(num,len(chars)+num):
            if chars[y] != A[x]:
                return A[x]
            else:
                y+=1
    else:
        num = a.index(chars[0])
        y = 0
        for x in range(num,len(chars)+num):
            if chars[y] != a[x]:
                return a[x]
            else:
                y+=1
            