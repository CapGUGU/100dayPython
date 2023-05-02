print("Welcome to the tip calculator")
totalBill = float(input("What was the total bill? $"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
peopleNum = int(input("How many people to split the bill? "))

finalBill = totalBill * (1 + percentage/100)
finalBill = -round(-finalBill / peopleNum, 2)

finalBill = "{:.2f}".format(finalBill)
print(f"Each person should pay: ${finalBill}")