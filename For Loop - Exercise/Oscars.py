actName=input()
accademyPoint=float(input())
humanCount=int(input())
oscarPoint=1250.50
actPoint=accademyPoint
for i in range(0,humanCount,1):
    cName=input()
    cPoints=float(input())
    actPoint+=(len(cName)*cPoints)/2
    if actPoint>=oscarPoint:
        print(f"Congratulations, {actName} got a nominee for leading role with {actPoint:.1f}!")
        exit(1)

print(f"Sorry, {actName} you need {oscarPoint-actPoint:.1f} more!")
