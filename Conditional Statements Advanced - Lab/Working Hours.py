weekDay={
"monday":1,
"tuesday":2,
"wednesday":3,
"thursday":4,
"friday":5,
"saturday":6,
"sunday":7
}
hour=int(input())
day=input().lower()
if hour>=10 and hour<=18 and weekDay[day]>0 and weekDay[day]<7:
    print("open")
else:
    print("closed")