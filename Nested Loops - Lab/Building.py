levelCount=int(input())
roomCount=int(input())
for level in range(levelCount,0,-1):
    for room in range(0,roomCount,1):
        if(level%2==0 and level!=levelCount):
            print("O{0}{1} ".format(level,room),end="")
        elif(level==levelCount):
            print("L{0}{1} ".format(level,room),end="")
        else:
            print("A{0}{1} ".format(level,room),end="")
    print("")
