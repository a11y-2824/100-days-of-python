from getpass import getpass as input

print("""
EPIC ROCK PAPER SCISSORS BATTLE
____________________________________________________

Please select your move
R for Rock 
P for Paper
S for Scissors

""")

player1_score = 0
player2_score = 0


while True:
  
  player1 = input("Player 1> ")
  player2 = input("Player 2> ")
  if player1 == 'R' and player2 == 'R':
    print("It's a tie. Try again")
  elif player1 == 'S' and player2 == 'S':
    print("It's a tie. Try again")
  elif player1 == 'P' and player2 == 'P':
    print("It's a tie. Try again")
  elif player1 == 'R' and player2 == 'S':
    print("Player 1 wins. Player 1's rock destroys player 2's scisors. ")
    player1_score += 1
  elif player1 == 'S' and player2 == 'R':
    print("Player 2 wins. Player 2's rock destroys player 1's scisors. ")
    player2_score += 1
  elif player1 == 'R' and player2 == 'P':
    print("Player 2 wins. Player 2's paper covers player 1's rock. ")
    player2_score += 1
  elif player1 == 'P' and player2 == 'R':
    print("Player 1 wins. Player 1's paper covers player 2's rock. ")
    player1_score += 1
  elif player1 == 'P' and player2 == 'S':
    print("Player 2 wins. Player 2's scissors cuts player 1's paper. ")
    player2_score += 1
  elif player1 == 'S' and player2 == 'P':
    print("Player 1 wins. Player 1's scissors cuts player 2's scisors. ")
    player1_score += 1
  else:
    print("Error! invalid input")


  if player1_score == 3:
    print("Player 1 wins this round")
    print("Goodbye, see you next game")
    exit()
       
  elif player2_score == 3:
    print("Player 2 wins this round")
    print("Goodbye, see you next game")
    exit()
  else:   
    continue
