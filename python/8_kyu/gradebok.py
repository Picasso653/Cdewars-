def get_grade(s1, s2, s3):
    avg = (s1+s2+s3)/3
    if 0<=avg<60:   return "F"
    if 60<=avg<70:  return 'D'
    if 70<=avg<80:  return 'C'
    if 80<=avg<90:  return 'B'
    if avg>=90:    return 'A'