penCount=int(input())
markerPacCount=int(input())
clean=int(input())
percentDiscount=int(input())/100
penPrice=5.80
markerPackPrice=7.20
cleanPrice=1.20
total=((penPrice*penCount)+(markerPackPrice*markerPacCount)+(cleanPrice*clean))
total-=total*percentDiscount
print(total)