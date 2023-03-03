def fizzbuzz(n):
    fizzy_numbers = []
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            fizzy_numbers.append('FizzBuzz')
        elif i%3==0:
            fizzy_numbers.append('Fizz')
        elif i%5==0:
            fizzy_numbers.append('Buzz')
        else:
            fizzy_numbers.append(i)
        i += 1
    return fizzy_numbers