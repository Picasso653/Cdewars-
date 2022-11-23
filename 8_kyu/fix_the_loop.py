def list_animals(animals):
    list = ''
    n=1
    for i in animals:
        list +=  str(n)+'. '+i+'\n'
        n+=1
    return list