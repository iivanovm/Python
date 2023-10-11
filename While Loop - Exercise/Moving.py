h=int(input())
w=int(input())
l=int(input())
cubic=h*l*w
command=""
isFull=0

while command!="Done":
    command=input()
    if(command!="Done"):
        cubic-=int(command)
        if(cubic<0):
            isFull=1
            break
if(isFull==1):
    print(f"No more free space! You need {abs(cubic)} Cubic meters more.")
else:
    print(f"{cubic} Cubic meters left.")
