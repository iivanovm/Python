budeget=float(input())
numberVc=int(input())
priceList={
    "videoCart":250,
    "cpu":(numberVc*250)*0.35,
    "ram":(numberVc*250)*0.1
}
numberCPU=int(input())
numberRAM=int(input())
total=(numberVc*priceList["videoCart"])+(numberCPU*priceList["cpu"])+(numberRAM*priceList["ram"])
if(numberVc>numberCPU):
    total-=total*0.15
if(budeget>=total):
    print(f"You have {budeget-total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total-budeget:.2f} leva more!")