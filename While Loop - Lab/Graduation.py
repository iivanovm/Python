grade = 0
stNegativeGrade = 0
studentName = input()
studentsum = 0
while grade < 12:
    currentGrade = float(input())
    if (currentGrade < 4):
        stNegativeGrade += 1
        if (stNegativeGrade == 2):
            break
        grade += 1
    else:
        grade += 1
        studentsum += currentGrade

if grade == 12:
    print(f"{studentName} graduated. Average grade: {studentsum / grade:.2f}")
else:
    print(f"{studentName} has been excluded at {grade} grade")
