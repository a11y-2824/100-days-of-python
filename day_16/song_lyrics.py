print("""
Fill in the blank lyrics!

""")
while True:
  answer = input("The _______ on the bus go round and round\n")
  if answer == "wheels":
    print("That's correct!")
    break
  else:
    print("Nope, try again")
    print("Hint: Nursery ryhme")
    print()
