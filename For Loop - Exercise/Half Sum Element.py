import sys

n=int(input())
maxNum=-sys.maxsize
sumNum=0
for i in range(0,n):
    currentNumber=int(input())
    if(maxNum<currentNumber):
        maxNum=currentNumber
    sumNum+=currentNumber
if(sumNum-maxNum==maxNum):
    print(f"Yes\nSum = {maxNum}")
else:
    print(f'No\nDiff = {abs(maxNum-(sumNum-maxNum))}')