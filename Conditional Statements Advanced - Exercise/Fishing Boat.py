boatPrice = {
    "Spring": 3000, "Summer": 4200, "Autumn": 4200, "Winter": 2600
}
budget=float(input())
season=input()
fishManCount=int(input())
total=0
total=boatPrice[season]
if(fishManCount<=6):
    total-=total*0.1
elif(fishManCount>6 and fishManCount<=11):
    total-=total*0.15
elif(fishManCount>12):
    total-=total*0.25


if(season!="Autumn" and fishManCount%2==0):
    total-=total*0.05

if(budget>=total):
    print(f"Yes! You have {budget-total:.2f} leva left.")
else:
    print(f"Not enough money! You need {total-budget:.2f} leva.")