budget = float(input())
season = input()
destination = ""
bgPrice = {
    "summer": 0.30,
    "winter": 0.70
}
bkPrice = {
    "summer": 0.40,
    "winter": 0.80
}

night = {
    "summer": "Camp",
    "winter": "Hotel"
}

nw=night[season]
tripPrice = 0
if budget <= 100:
    destination = "Bulgaria"
    total = budget * bgPrice[season]
elif budget <= 1000 and budget > 100:
    destination = "Balkans"
    total = budget * bkPrice[season]
else:
    destination = "Europe"
    total = budget * 0.90
    nw="Hotel"



print(f"Somewhere in {destination}")
print(f"{nw} - {total:.2f}")
