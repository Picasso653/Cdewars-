def solution(start, finish):  
    count = 0
    while start < finish:
        if (start + 3) > finish:
            start += 1
        else:
            start += 3
        count += 1
    return count
