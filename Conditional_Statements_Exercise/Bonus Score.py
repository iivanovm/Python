number=int(input())
bonuspoints=0
vip=0
if number<=100:
    bonuspoints=5
elif number>1000:
    bonuspoints=0.1*number
else:
    bonuspoints=0.2*number
if(number%2==0):
    vip+=1
elif(number%10==5):
    vip+=2

print(bonuspoints+vip)
print(vip+bonuspoints+number)