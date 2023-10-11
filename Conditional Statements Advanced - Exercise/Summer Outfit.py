degree = int(input())
timeOfday = input()
Outfit = ""
Shoes = ""
if (timeOfday == "Morning"):
    if 10 <= degree <= 18:
        Outfit = "Sweatshirt"
        Shoes = "Sneakers"
    elif 18 < degree <= 24:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    else:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
elif (timeOfday == "Afternoon"):
    if 10 <= degree <= 18:
        Outfit = "Shirt"
        Shoes = "Moccasins"
    elif 18 < degree <= 24:
        Outfit = "T-Shirt"
        Shoes = "Sandals"
    else:
        Outfit = "Swim Suit"
        Shoes = "Barefoot"
elif (timeOfday == "Evening"):
    Outfit = "Shirt"
    Shoes = "Moccasins"


print(f"It's {degree} degrees, get your {Outfit} and {Shoes}.")
