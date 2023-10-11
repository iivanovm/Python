import sys
n=int(input())
maxNumber=-sys.maxsize
minNumber=sys.maxsize
for number in range(0,n,1):
    currentNumber=int(input())
    if(maxNumber<currentNumber):
        maxNumber=currentNumber
    if(minNumber>currentNumber):
        minNumber=currentNumber

print(f"Max number: {maxNumber}\nMin number: {minNumber}")
