import math

recordInSeconds=float(input())
lenghtInMeters=float(input())
timeSwimingOneMeter=float(input())
playerTime=lenghtInMeters*timeSwimingOneMeter
playerSlowTime=math.floor(lenghtInMeters/15)
playerSlowTime*=12.5
playerTime+=playerSlowTime
if(playerTime<recordInSeconds):
    print(f"Yes, he succeeded! The new world record is {playerTime:.2f} seconds.")
else:
    print(f"No, he failed! He was {playerTime-recordInSeconds:.2f} seconds slower.")