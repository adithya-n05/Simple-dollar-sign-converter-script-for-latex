x = input("Enter string:")

dollarlist = [""]
stringlist = []

for i in x:
    stringlist.append(i)

for i in range(len(stringlist)):
    if stringlist[i] == "$":
        if "$" in dollarlist:
            stringlist[i] = "\)"
            dollarlist = []
        else:
            stringlist[i] = "\("
            dollarlist = ["$"]

y = ""

for i in stringlist:
    y = y + i

print(y)
