city = input().lower()
commission = float(input())
total = 0
if (city != "sofia" and city != "varna" and city != "plovdiv" or commission<0):
    print("error")
else:
    if 0 <= commission <= 500 and city == "sofia":
        total = commission * 0.05
    elif 500 < commission <= 1000 and city == "sofia":
        total = commission * 0.07
    elif 1000 < commission <= 10000 and city == "sofia":
        total = commission * 0.08
    elif commission > 10000 and city == "sofia":
        total = commission * 0.12
    elif 0 <= commission <= 500 and city == "varna":
        total = commission * 0.045
    elif 500 < commission <= 1000 and city == "varna":
        total = commission * 0.075
    elif 1000 < commission <= 10000 and city == "varna":
        total = commission * 0.1
    elif commission > 10000 and city == "varna":
        total = commission * 0.13
    elif 0 <= commission <= 500 and city == "plovdiv":
        total = commission * 0.055
    elif 500 < commission <= 1000 and city == "plovdiv":
        total = commission * 0.08
    elif 1000 < commission <= 10000 and city == "plovdiv":
        total = commission * 0.12
    elif commission > 10000 and city == "plovdiv":
        total = commission * 0.145

    print(f"{total:.2f}")