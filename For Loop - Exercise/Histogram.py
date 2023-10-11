p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
n = int(input())
for num in range(0, n, 1):
    currentNumber = int(input())
    if currentNumber < 200:
        p1 += 1
    elif currentNumber >= 200 and currentNumber <= 399:
        p2 += 1
    elif currentNumber >= 400 and currentNumber <= 599:
        p3 += 1
    elif currentNumber >= 600 and currentNumber <= 799:
        p4 += 1
    else:
        p5 += 1

print(f"{p1 / n *100:.2f}%\n{p2 / n * 100:.2f}%\n{p3 / n * 100:.2f}%\n{p4 / n * 100:.2f}%\n{p5 / n * 100:.2f}%")
