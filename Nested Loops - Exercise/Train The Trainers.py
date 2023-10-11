judge = int(input())
presentaionName = ""
courseAverageGrade = 0
courseCount = 0
while presentaionName != "Finish":
    presentaionName = input()
    if (presentaionName == "Finish"):
        break
    else:
        averageGrade = 0
    for grade in range(0, judge, 1):
        currentGrade = float(input())
        averageGrade += currentGrade

    averageGrade /= judge
    courseAverageGrade += averageGrade
    courseCount += 1
    print(f"{presentaionName} - {averageGrade:.2f}.")

print(f"Student's final assessment is {courseAverageGrade / courseCount:.2f}.")
