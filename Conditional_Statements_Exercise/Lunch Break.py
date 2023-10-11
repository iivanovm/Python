import math

movie=input()
movieLenght=int(input())
breakTime=int(input())
lounchtime=breakTime*0.125
freetime=breakTime*0.25
leftTime=breakTime-lounchtime-freetime
if(leftTime>=movieLenght):
    print(f"You have enough time to watch {movie} and left with {leftTime-movieLenght:.0f} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie}, you need {math.ceil(movieLenght-leftTime)} more minutes.")