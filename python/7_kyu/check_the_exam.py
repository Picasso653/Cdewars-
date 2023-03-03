def check_exam(arr1,arr2):
    total_score = 0
    for i in range(0,len(arr1)):
        if arr2[i] == "":
            continue
        if arr1[i] == arr2[i]:
            total_score += 4
        else:
            total_score -= 1
    return total_score if total_score > 0 else 0