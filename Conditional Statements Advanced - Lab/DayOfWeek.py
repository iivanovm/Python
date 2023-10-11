number=int(input())
weekDay={
1:"Monday",
2:"Tuesday",
3:"Wednesday",
4:"Thursday",
5:"Friday",
6:"Saturday",
7:"Sunday"
}
if 0 > number or number < 8:
    print(weekDay[number])
else:
    print("Error")
