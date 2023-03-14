import random

print("""
Guess the Number
==========================================

I have picked a number between 1 and 100. Can you geuss the number?

""")


counter = 0
myNumber = random.randint(1,10)
while True:
  answer = (int(input("What is your guess? ")))

  if answer > myNumber:
    print("That's too high")
    counter += 1
  elif answer < myNumber:
    print("That's too low")
    counter += 1
  elif answer == myNumber:
    print("That's correct!")
    counter += 1
  else:
    print("Invalid answer")
    exit()
  
  if answer == myNumber:
    print("It only took you", counter, "guesses to get correct")
    exit()
  else:
    continue
    
