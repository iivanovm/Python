budget=float(input())
statistsCount=int(input())
priceCl=float(input())
dekor=budget*0.1
cl=statistsCount*priceCl
if(statistsCount>150):
    cl-=cl*0.10
total=dekor+cl
if(budget<total):
    print("Not enough money!")
    print(f"Wingard needs {total-budget:.2f} leva more.")
else:
    print("Action!")
    print(F"Wingard starts filming with {budget-total:.2f} leva left.")