tabCount = int(input())
salary = float(input())
blockSite = {
    "Facebook": 150,
    "Instagram": 100,
    "Reddit": 50
}
for i in range(0, tabCount, 1):
    currentTab = input()
    salary -= blockSite.setdefault(currentTab,0)
    if (salary <= 0):
        print("You have lost your salary.")
        exit(1)

print(f"{salary:.0f}")
