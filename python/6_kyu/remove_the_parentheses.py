def remove_parentheses(s):
    res = ''
    count = 0
    for i in s:
        if i == '(':
            count += 1
        elif i == ')':
            count -= 1
        elif count == 0:
            res += i
    return res