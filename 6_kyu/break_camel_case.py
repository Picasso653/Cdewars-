def solution(s):
    s_listed = []
    start = 0
    for i,j in enumerate(s):
        if j.isupper():
            s_listed.append(s[start:i])
            start = i
    return ' '.join(s_listed) + ' ' + s[start:]