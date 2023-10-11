import  math
tCount=int(input())
startPoints=int(input())
averagePoints=0
winGame=0
positionPoints={
    "W":2000,
    "F":1200,
    "SF":720
}
for t in range(0,tCount,1):
    currentT=input()
    startPoints+=positionPoints[currentT]
    averagePoints+=positionPoints[currentT]
    if currentT=="W":
        winGame+=1
print(f"Final points: {startPoints}\nAverage points: {math.floor(averagePoints/tCount):.0f}\n{winGame/tCount*100:.2f}%")