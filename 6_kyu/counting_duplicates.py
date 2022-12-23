def duplicate_count(text):
    return len([i for i in set(text.lower()) if text.lower().count(i) > 1])