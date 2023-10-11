hours=int(input())
min=int(input())+15
if min>59:
    hours+=1
    if hours>23:
        hours=0
    min-=60
print(f'{hours}:{min:02d}')