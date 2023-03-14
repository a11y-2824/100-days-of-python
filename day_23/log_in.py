# using def function to create a log in system
print("""
REPLIT log in page
--------------------------------

Please input username and password

""")

def logins():
  while True:
    userName = input("What is your username? ")
    password = input("what is your password? ")
    if userName == "Anne" and password == "a11y":
      print("Welcome to Replit!")
      exit()
    else:
      print("I don't recognize that username or password. Try again!")
      print()
    continue

logins() 
