start = int(input())
end = int(input())
magicNumber = int(input())
isFound = 0
combinationCount = 0
for first in range(start, end + 1, 1):
    for second in range(start, end + 1, 1):
        combinationCount += 1
        if (first + second) == magicNumber:
            isFound = 1
            break
    if (isFound == 1):
        break

if(isFound==1):
    print(f"Combination N:{combinationCount} ({first} + {second} = {first+second})")
else:
    print(f"{combinationCount} combinations - neither equals {magicNumber}")