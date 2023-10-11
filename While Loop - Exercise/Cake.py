cakeL = int(input())
cakeW = int(input())
cake = cakeW * cakeL
cakeOver = 0
command = ""
while command != "STOP":

    command = input()
    if (command != "STOP"):

        if (cake < int(command)):
            cakeOver = 1
            break
        else:
            cake -= int(command)

if cakeOver == 1:
    print(f"No more cake left! You need {int(command) - cake} pieces more.")
else:
    print(f"{cake} pieces are left.")
