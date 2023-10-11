number=int(input())
curent=1
isBig=0
for row in range(1,number+1,1):
    for col in range(1,row+1):
        if curent>number:
            isBig=1
            break
        print(str(curent)+ ' ',end='')
        curent+=1
    if isBig==1:
        break
    print()