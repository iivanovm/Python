import math

figureType=input()
area=0
if figureType=='square':
    a=float(input())
    area=a*a
elif figureType=='rectangle':
    a = float(input())
    b=float(input())
    area=a*b
elif figureType=='circle':
    a = float(input())
    area=math.pi*a*a
elif figureType=='triangle':
    a = float(input())
    b=float(input())
    area=1/2*a*b

print(f"{area:.3f}")