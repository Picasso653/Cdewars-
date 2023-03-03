def expanded_form(num):
    whole_number = str(num).split('.')[0]
    dig_w = len(whole_number)
    decimal_number = str(num).split('.')[-1]
    dig_d = len(decimal_number)
    x = ' + '.join([j +'0'*(dig_w-1-i) for i,j in enumerate(list(whole_number)) if j != '0'])
    y = ' + '.join([l +'/'+'1'+'0'*(k+1) for k,l in enumerate(decimal_number) if l!='0'])
    return x + ' + ' + y if x != '' else y