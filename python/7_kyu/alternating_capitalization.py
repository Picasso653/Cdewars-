def capitalize(s):
    return [''.join([s[i].upper() if i%2==0 else s[i] for i in range(0,len(s))]),''.join([s[i].upper() if i%2==1 else s[i] for i in range(0,len(s))])]
        