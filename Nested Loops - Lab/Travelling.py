destination=""
currentMoney=0
while destination!="End":
    destination=input()
    if destination=="End":
        break
    neededMoney=float(input())
    currentMoney=0
    while neededMoney>currentMoney:
        money=float(input())
        currentMoney+=money
    print(f"Going to {destination}!")



