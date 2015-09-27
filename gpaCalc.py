def grade_point_calc(creditHr, grade):
    print(creditHr, grade)
    return round(creditHr,2) * round(grade,2)

def gpa_calc(gpa_list):
    totalGradePoint = 0
    totalCredit = 0
    for pair in gpa_list:
        totalGradePoint += grade_point_calc(pair[0], pair[1])
        totalCredit += pair[0]
    if(totalCredit == 0):
        return 0
    gpa = totalGradePoint/totalCredit
    return gpa