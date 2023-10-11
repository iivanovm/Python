class calculator:
    isEven = 0

    def __init__(self, first, second, w):
        self.first = first
        self.second = second
        self.w = w

    def calc(self):
        if self.w == "+":
            isEven = (self.first + self.second) % 2 == 0
            r = ""
            if isEven:
                r = "even"
            else:
                r = "odd"
            result = f"{self.first} {self.w} {self.second} = {self.first + self.second} - {r}"
        elif self.w == "-":
            isEven = (self.first - self.second) % 2 == 0
            r = ""
            if isEven:
                r = "even"
            else:
                r = "odd"
            result = f"{self.first} {self.w} {self.second} = {self.first - self.second} - {r}"
        elif self.w == "*":
            isEven = (self.first * self.second) % 2 == 0
            r = ""
            if isEven:
                r = "even"
            else:
                r = "odd"
            result = f"{self.first} {self.w} {self.second} = {(self.first * self.second)} - {r}"
        elif self.w == "/":
            if (self.second == 0):
                result = f"Cannot divide {self.first} by zero"
            else:
                result = f"{self.first} {self.w} {self.second} = {(self.first / self.second):.2f}"
        elif self.w == "%":
            if (self.second == 0):
                result = f"Cannot divide {self.first} by zero"
            else:
                result = f"{self.first} {self.w} {self.second} = {(self.first % self.second)}"
        return result


numberOne = int(input())
numberTwo = int(input())
cchar = input()
calc = calculator(numberOne, numberTwo, cchar).calc()
print(calc)
