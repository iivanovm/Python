number = int(input())
count = 0
for first in range(0, number + 1, 1):
    for second in range(0, number + 1, 1):
        for third in range(0, number + 1, 1):
            if (first + second + third == number):
                count += 1
print(count)