print("""
Animal sounds
==============================

Hi, welcome to animal sound
""")
exit = ""
while exit != "yes":
  print()
  sound = input("What animal sound do you want to hear? ")
  if sound == "cow":
    print("A cow goes moo")
  elif sound == 'dog':
    print("A dog goes woof!")
  elif sound == 'cat':
    print("A cat goes meow!")
  elif sound == 'dog':
    print("A duck goes quack!")
  else:
    print("Sorry, I do not know that animal sound.")
  exit = input("Do you want to exit? ")
