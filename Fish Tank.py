lenght=int(input())
weight=int(input())
height=int(input())
percent=float(input())
aquariumVolume=lenght*height*weight*0.001
toLiter=(percent/100)
neededLiters=aquariumVolume*(1-toLiter)
print(neededLiters)