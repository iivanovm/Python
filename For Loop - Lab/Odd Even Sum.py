n=int(input())
leftSum=0
rightSum=0
for number in range(0,n,1):
    currentNumber=int(input())
    if(number%2==0):
        leftSum+=currentNumber
    elif(number%2!=0):
        rightSum+=currentNumber

if(leftSum==rightSum):
    print(f"Yes\nSum = {leftSum}")
else:
    print(f"No\nDiff = {abs(leftSum-rightSum)}")