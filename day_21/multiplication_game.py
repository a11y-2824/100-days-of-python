# A game to test out multiplication tables

print("""
Math Game
-------------------------------------


""")

multiples = int(input("Choose your multiples: "))
counter = 0

for i in range(1, 6):
  correctAnswer = i*multiples
  print(i, "x", multiples)
  userAnswer = int(input("= "))
  if userAnswer == correctAnswer:
    print("That is correct!")
    counter +=1
  else:
   print("That is incorrect. The correct answer is", correctAnswer)
  print()

print("You got", counter, "answers correct")
