myBill = float(input("What was the bill?: "))

# Include tip
total = myBill*1.15
numberOfPeople = int(input("How many people?: "))
answer = total / numberOfPeople
answer = round(answer, 2)
print("You all owe", answer)
