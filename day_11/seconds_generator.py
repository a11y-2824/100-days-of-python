print("""
Coverting values to seconds
_________________________________

""")
answer = int(input("""
Hi , welocme to the seconds conveter. 
Please select an option (input numbers only)

1. How many seconds are in a minute?
2. How many seconds are in a hour?
3. How many seconds are in a day?
4. How many seconds are in a month?
5. How many seconds are in a normal year?
6. How many seconds are in a leap year?


"""))
minute = 60*1
hour = 60 * minute
day = 24 * hour
month = 31 * day
regYear = 365 * day
leapYear = 366 * day

if answer == 1:
  print("There are", minute, "seconds in a second")
elif answer == 2:
  print("There are", hour, " seconds in a hour")
elif answer == 3:
  print("There are", day, "seconds in a day")
elif answer == 4:
  print("There are", month, "seconds in a month")
elif answer == 5:
  print("There are", regYear, "seconds in a regular year")
elif answer == 6:
  print("There are ", leapYear, "in a leap year")
else:
  print("Error- Invalid input")
