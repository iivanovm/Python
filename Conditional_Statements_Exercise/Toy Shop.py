price={
    "puuzle":2.60,
    "barbie":3,
    "bear":4.10,
    "minion":8.20,
    "truck":2
}
totalPrice=0.00
tripPrice=float(input())
puzzle=int(input())
bbarbie=int(input())
bbear=int(input())
minions=int(input())
trucks=int(input())
totalToysCount=puzzle+bbear+bbarbie+minions+trucks
total=(puzzle*price["puuzle"])+(bbarbie*price["barbie"])+(bbear*price["bear"])+(minions*price["minion"])+(trucks*price["truck"])
if(totalToysCount>=50):
    total-=total*0.25
total-=total*0.1
totalPrice=total
if(tripPrice>totalPrice):
    print(f"Not enough money! {tripPrice-totalPrice:.2f} lv needed.")
else:
    print(f"Yes! {totalPrice-tripPrice:.2f} lv left.")
