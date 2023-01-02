def solution(s):
    if s == "":
        return []
    return [s[i-2:i] for i in range(2,len(s)+1,2)] if len(s)%2 ==0 else solution(s+'_')