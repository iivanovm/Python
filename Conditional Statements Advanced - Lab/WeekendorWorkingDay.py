weekDay={
"monday":1,
"tuesday":2,
"wednesday":3,
"thursday":4,
"friday":5,
"saturday":6,
"sunday":7
}
dd=input().lower()
if dd!="monday" and dd!="tuesday" and dd!="wednesday"and dd!="thursday"and dd!="friday" and dd!="saturday" and dd!="sunday" :
    print("Error")
else:
    if  weekDay[dd]>0 and weekDay[dd]<6:
        print("Working day")
    else:
        print("Weekend")