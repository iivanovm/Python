countNegativeGrade = int(input())
count = 0
gradeSum = 0
negativeCount = 0
needBreak = 0
lastProblem = ""
while negativeCount < countNegativeGrade:
    problemName = input()
    if (problemName == "Enough"):
        break
    grade = float(input())
    if grade <= 4:
        negativeCount += 1
        if(negativeCount>=countNegativeGrade):
            needBreak=1

    count += 1
    gradeSum += grade
    lastProblem=problemName

if(needBreak==1):
    print(f"You need a break, {negativeCount} poor grades.")
else:
    print(f"Average score: {gradeSum/count:.2f}\nNumber of problems: {count}\nLast problem: {lastProblem}")