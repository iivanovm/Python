isPrime = False
primeSum = 0
notPrimeSum = 0

def checkP(number):
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True

command = ""
while command != "stop":
    command = input()
    if (command == "stop"):
        break
    if int(command) < 0:
        print(f"Number is negative.")
    elif checkP(int(command)):
        primeSum += int(command)
    else:
        notPrimeSum += int(command)

print(f"Sum of all prime numbers is: {primeSum}\nSum of all non prime numbers is: {notPrimeSum}")
