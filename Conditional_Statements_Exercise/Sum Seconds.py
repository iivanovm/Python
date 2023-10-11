import math

first=int(input())
second=int(input())
third=int(input())
total=first+second+third
minutes=math.floor(total/60)
secondns=total%60
print(f'{minutes}:{secondns:02d}')

