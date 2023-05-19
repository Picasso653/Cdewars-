from collections import Counter


def scramble(s1, s2):
    freq_table = Counter(s1)
    for char in s2:
        if freq_table[char] == 0:
            return False
        freq_table[char] -= 1
    return True