start=int(input())
end=int(input())
for number in range (start,end+1,1):
    oddSum=0
    evenSum=0
    for index, digit in enumerate(str(number)):
        if index%2==0:
            oddSum+=int(digit)
        else:
            evenSum+=int(digit)
    if evenSum==oddSum:
        print(number,end=' ')
