def is_valid_walk(walk):
    return True if len(walk)== 10 and walk.count('n')==walk.count('s') and walk.count('e')==walk.count('w') else False