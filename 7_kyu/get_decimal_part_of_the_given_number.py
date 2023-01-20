def get_decimal(n): 
    return float('0.'+str(n).split('.')[-1]) if '.' in str(n) else 0