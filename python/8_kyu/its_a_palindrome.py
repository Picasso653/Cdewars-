def is_palindrome(s):
    return(list(s.lower()) == list(s.lower()[::-1]))