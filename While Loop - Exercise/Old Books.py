searchBook = input()
stop = "No More Books"
currentBook = ""
checkBooks = 0
isFound = 0
while currentBook != stop:
    currentBook = input()
    if (currentBook != searchBook):
        checkBooks += 1
    else:
        isFound = 1
        break

if (isFound == 1):
    print(f"You checked {checkBooks} books and found it.")
else:
    print(f"The book you search is not here!\nYou checked {checkBooks-1} books.")
