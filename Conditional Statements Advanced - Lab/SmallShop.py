from unicodedata import decimal

priceSofia = {
    "coffee": 0.50,
    "water": 0.80,
    "beer": 1.20,
    "sweets": 1.45,
    "peanuts": 1.60
}
pricePlovdiv = {
    "coffee": 0.40,
    "water": 0.70,
    "beer": 1.15,
    "sweets": 1.30,
    "peanuts": 1.50
}
priceVarna = {
    "coffee": 0.45,
    "water": 0.70,
    "beer": 1.10,
    "sweets": 1.35,
    "peanuts": 1.55
}
product=input().lower()
city=input()
quantity=float(input())
price=0
if city=="Sofia":
    print(quantity*priceSofia[product])
elif city=="Plovdiv":
    print(quantity*pricePlovdiv[product])
elif city=="Varna":
    print(quantity*priceVarna[product])
