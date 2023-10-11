neededMoney = float(input())
currentMoney = float(input())
spendCount = 0
totalCount = 0
while currentMoney < neededMoney and spendCount < 5:
    action = input()
    money = float(input())
    totalCount += 1
    if (action == "spend"):
        spendCount += 1
        if (currentMoney < money):
            currentMoney = 0
        else:
            currentMoney -= money
    else:
        currentMoney += money
        spendCount = 0

if currentMoney >= neededMoney:
    print(f"You saved the money for {totalCount} days.")
else:
    print(f"You can't save the money.\n{totalCount}")
