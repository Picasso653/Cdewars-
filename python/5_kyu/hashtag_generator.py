def generate_hashtag(s):
    if s == '' or len(s.strip())>=140:
        return False
    hash_tag = '#'
    for word in s.split(' '):
        hash_tag += word.title()
    return hash_tag