musala=0
monblan=0
kili=0
k2=0
everest=0
psum=0
groupCount=int(input())
for currentGroup in range(0,groupCount,1):
    peopleInCurrentGroup=int(input())
    psum+=peopleInCurrentGroup
    if peopleInCurrentGroup<=5:
        musala+=peopleInCurrentGroup
    elif peopleInCurrentGroup>5 and peopleInCurrentGroup<=12:
        monblan+=peopleInCurrentGroup
    elif peopleInCurrentGroup>12 and peopleInCurrentGroup<=25:
        kili+=peopleInCurrentGroup
    elif peopleInCurrentGroup>25 and peopleInCurrentGroup<=40:
        k2+=peopleInCurrentGroup
    else:
        everest+=peopleInCurrentGroup

print(f"{musala/psum*100:.2f}%\n{monblan/psum*100:.2f}%\n{kili/psum*100:.2f}%\n{k2/psum*100:.2f}%\n{everest/psum*100:.2f}%")