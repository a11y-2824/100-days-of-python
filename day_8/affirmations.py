print("""
Welcome to money manifestation affirmations
================================================


Let's get started!""")
name = input("What is your name? ")
print()
scale = int(input("On a scale of 1-10. How are you feeling today? (1 = sad, 10 = happy\n) "))
if scale == 1:
  print("I release all negative energy over money.")
elif scale == 2:
  print("I control money, money doesn’t control me.")
elif scale == 3:
  print("My finances don’t scare me because I have a plan")
elif scale == 4:
  print("It is within my power to create a successful financial future.")
elif scale == 5:
  print("My income can exceed my expenses.")
elif scale == 6:
  print("There are countless opportunities to make more money in my life.")
elif scale == 7:
  print("I am on my way to becoming wealthy.")
elif scale == 8:
  print("I can make my dreams a reality with careful budgeting.")
elif scale == 9:
  print("I have the discipline to make hard financial choices now to enjoy an easy life later.")
elif scale == 10:
  print("Making choices to build wealth today can allow me to build the life I desire.")
elif scale >= 11:
  print("I deserve to be paid a fair wage for my skills and time.")
elif scale <= 0:
  print("With hard work and creativity, I can build the financial picture that I desire.")
else:
  print("Please input a number")
