import sys

command=""
maxNumber=sys.maxsize
while command!="Stop":
    command=input()
    if command!="Stop":
        if maxNumber>int(command):
            maxNumber=int(command)

print(maxNumber)