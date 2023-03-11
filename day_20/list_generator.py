#Generate a list using input from users

print("""
List Generator
----------------------------------------

Please input the followig details
""")

start = int(input("Start the list at: "))
stop = int(input("End the list at: "))
increase = int(input("Increment between values: "))

for i in range(start, stop, increase):
  print(i)
