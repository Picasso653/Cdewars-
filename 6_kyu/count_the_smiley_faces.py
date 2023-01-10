def count_smileys(arr):
#     let's count
    count = 0
    nose = [i for i in arr if len(i)==3]
    anti_nose = [j for j in arr if len(j)==2]
    a = sum([1 for x in anti_nose if x in [':)',';)',':D',';D'] ])
    b = sum([1 for y in nose if y in [':-)',':~)',';-)',';~)',':-D',';-D',':~D',';~D'] ])
    return a+b