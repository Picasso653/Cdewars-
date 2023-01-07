def comp(array1, array2):
    if array1==[] and array2==[]:
        return True
    elif array1==[] or array2==[]:
        return False
    positive = [abs(j) for j in array1]
    a,b = sorted(positive),sorted(array2)
    for i in range(0,len(a)):
        if a[i]**2 != b[i]:
            return False
    return True
	