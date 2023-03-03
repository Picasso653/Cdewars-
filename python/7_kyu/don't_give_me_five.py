def dont_give_me_five(start,end):
    return len([n for n in range(start, end+1) if '5' not in str(n)])