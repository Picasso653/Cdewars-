def is_pangram(s):
    import string
    return True if string.ascii_lowercase == ''.join(sorted(set([i for i in s.lower() if i in string.ascii_lowercase]))) else False