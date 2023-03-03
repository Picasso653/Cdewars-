def solution(digits):
    answer = 0
    i=0
    while i < len(digits):
        number = digits[i: i+5]
        i +=1
        if int(number) > answer:
            answer = int(number)
    return answer