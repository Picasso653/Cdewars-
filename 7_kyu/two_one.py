def longest(a1, a2):
    chars = set(a1 + a2)
    sorted_chars = sorted(chars, key=str.lower)
    sorted_string = "".join(sorted_chars)

    return sorted_string
