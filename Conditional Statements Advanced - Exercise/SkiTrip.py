days = int(input()) - 1
roomType = input()
feedback = input()

priceRoom = {
    "room for one person": 18.00,
    "apartment": 25.00,
    "president apartment": 35.00

}

fb = {
    "positive": 0.25,
    "negative": 0.10
}

if days < 10:
    dcount = 1  # 10 дни
elif days >= 10 and days <= 15:
    dcount = 2  # 10-15 дни
elif days > 15:
    dcount = 3  # >15 дни

class apartment:
    def __init__(self, dc, price):
        self.dc = dc
        self.price = price

    def calc(self):
        if self.dc == 1:
            total = self.price - (self.price * 0.30)
        elif self.dc == 2:
            total = self.price - (self.price * 0.35)
        elif self.dc == 3:
            total = self.price - (self.price * 0.50)
        return total


class pApart:
    def __init__(self, pdc, pprice):
        self.pdc = pdc
        self.pprice = pprice

    def calc(self):
        if self.pdc == 1:
            ptotal = self.pprice - (self.pprice * 0.10)
        elif self.pdc == 2:
            ptotal = self.pprice - (self.pprice * 0.15)
        elif self.pdc == 3:
            ptotal = self.pprice - (self.pprice * 0.20)
        return ptotal


class roomP:
    def __init__(self, pdc, pprice):
        self.pdc = pdc
        self.pprice = pprice

    def calc(self):
        if self.pdc == 1:
            rtotal = self.pprice - 0
        elif self.pdc == 2:
            rtotal = self.pprice - 0
        elif self.pdc == 3:
            rtotal = self.pprice - 0
        return rtotal


rt = {
    "apartment": apartment,
    "president apartment": pApart,
    "room for one person": roomP
}

price = days * priceRoom[roomType]
price = rt[roomType](dcount, price).calc()
if feedback == "positive":
    price += price * fb[feedback]
else:
    price -= price * fb[feedback]
print(f"{price:.2f}")
