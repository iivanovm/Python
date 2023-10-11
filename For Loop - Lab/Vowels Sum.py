points={
    "a":1,
    "e":2,
    "i":3,
    "o":4,
    "u":5
}

str=input()
totalSum=0
for char in str:
    totalSum+=int(points.setdefault(char,0))

print(totalSum)