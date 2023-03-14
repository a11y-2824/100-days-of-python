# A game that uses sub classes to create an infinity dice

import random

print("""
INFINITY DICE
----------------------------------------

This game allows you to roll a dice with any number of sides.
It will generate a new number each time

""")
sides = int(input("How many sides should the dice have? "))
reply = random.randint(1,sides)
print(reply)

def infinityDice(sides):
  while True:
    anotherTrial = input("Roll again? ")
    if anotherTrial == 'yes':
      answer = random.randint(1,sides)
      print(answer)
      continue
    else:
      exit()
  
infinityDice(sides)
