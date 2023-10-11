stopWord = "NoMoreMoney"
current = 0
total = 0
while current != stopWord:
    current = input()
    if (current != stopWord):

        if (float(current) < 0):
            print("Invalid operation!")
            break
        else:
            total += float(current)
            print(f"Increase: {float(current):.2f}")
print(f"Total: {total:.2f}")
