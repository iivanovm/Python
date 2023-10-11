num = int(input())


def isSpecialNumber(number, snum):
    isSn = 1
    for index, digit in enumerate(str(snum)):
        if int(digit) != 0:
            if number % int(digit) != 0:
                isSn = 0
                break
        elif int(digit) == 0:
            isSn = 0
            break
    return isSn

for i in range(1111, 9999 + 1, 1):
    if isSpecialNumber(num, i) == 1:
        print(str(i),'',end="")
