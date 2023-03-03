def number_joy(n):
    separate = list(str(n))
    digit_sum = 0
    for i in separate:
        digit_sum += int(i)
    x = n % digit_sum
    rev = str(digit_sum)[::-1]
    if x == 0:
        return int(rev) * digit_sum == n
    else:
        return False
        
   