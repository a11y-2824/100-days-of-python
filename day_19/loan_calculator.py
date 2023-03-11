# A client took out a loan of 1000 caluclate the loan interest every year for ten years

print("""
Loan Calculator
___________________________________

""")

loan = 1000
year = 0
for i in range (10):
  loan *=1.05
  year +=1
  print("Year", year, 'is', round(loan, 2))

