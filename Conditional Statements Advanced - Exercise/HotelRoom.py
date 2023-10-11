month = input()
day = int(input())
Stdio = 0
Apartment = 0
if month == "May" or month == "October":
    Studio = 50
    Apartment = 65
elif month == "June" or month == "September":

    Studio = 75.20
    Apartment = 68.70

elif month == "July" or month == "August":
    Studio = 76
    Apartment = 77


totalS = Studio * day
totalA = Apartment * day

if day > 14:
    totalA -= totalA * 0.1
    if (month == "June" or month == "September"):
        totalS -= totalS * 0.20
if month == "May" or month == "October":
    if day > 14:
        totalS -= totalS * 0.30
    elif day > 7 and day <= 14:
        totalS -= totalS * 0.05

print(f"Apartment: {totalA:.2f} lv.\nStudio: {totalS:.2f} lv.")