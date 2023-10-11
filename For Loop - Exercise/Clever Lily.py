lilyOld=int(input())
washmashinePrice=float(input())
toyPrice=int(input())
toysCount=0
liliMoney=0
gift=10
positiveCount=0
for year in range(1,lilyOld+1,1):
    if(year%2==0 and year>=2):
        liliMoney+=gift
        gift+=10
        positiveCount+=1
    elif(year%2!=0):
        toysCount+=1
liliMoney+=toysCount*toyPrice-positiveCount*1
if liliMoney>=washmashinePrice:
    print(f"Yes! {liliMoney-washmashinePrice:.2f}")
else:
    print(f"No! {washmashinePrice-liliMoney:.2f}")