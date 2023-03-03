def fake_bin(x):
    binary = ''
    for i in x:
        if int(i)>4:
            binary += "1"
        else:
            binary += '0'
        
    return binary