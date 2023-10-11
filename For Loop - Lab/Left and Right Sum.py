n=int(input())
leftSum=0
rightSum=0
for number in range(0,n*2,1):
    currentNumber=int(input())
    if number<n:
        leftSum+=currentNumber
    else:
        rightSum+=currentNumber
if(leftSum==rightSum):
    print(f"Yes, sum = {leftSum}")
else:
    print(f"No, diff = {abs(leftSum-rightSum)}")