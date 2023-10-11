flowerType = input()
flowerCount = int(input())
budget = float(input())
flowerPrice = {
    "Roses": 5,
    "Dahlias": 3.80,
    "Tulips": 2.80,
    "Narcissus": 3,
    "Gladiolus": 2.50
}
total = flowerCount * flowerPrice[flowerType]
if flowerType == "Roses" and flowerCount > 80:
    total -= total * 0.1
elif flowerType == "Dahlias" and flowerCount > 90:
    total -= total * 0.15
elif flowerType == "Tulips" and flowerCount > 80:
    total -= total * 0.15
elif flowerType == "Narcissus" and flowerCount < 120:
    total += total * 0.15
elif flowerType == "Gladiolus" and flowerCount < 80:
    total += total * 0.20

if (total > budget):
    print(f"Not enough money, you need {total - budget:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {flowerCount} {flowerType} and {budget - total:.2f} leva left.")
