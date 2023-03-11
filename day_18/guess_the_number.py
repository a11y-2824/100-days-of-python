print("""
Guess the Number
==========================================

I have picked a number between 1 and 100. Can you geuss the number?

""")
# The number is 75

counter = 0

while True:
  answer = (int(input("What is your guess? ")))
  if answer >= 76:
    print("That's too high")
    counter += 1
    
  elif answer <= 74:
    print("That's too low")
    counter += 1
  elif answer == 75:
    print("That's correct!")
    counter += 1
  else:
    print("Invalid answer")
    exit()

  if answer == 75:
    print("It only took you", counter, "guesses to get correct")
    exit()
  else:
    continue
    
