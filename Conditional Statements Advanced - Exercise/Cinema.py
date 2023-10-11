ticketPrice={
    "Premiere":12,
    "Normal":7.50,
    "Discount":5.00
}
typeProject=input()
rows=int(input())
columns=int(input())
total=ticketPrice[typeProject]*rows*columns
print(f"{total:.2f} leva")