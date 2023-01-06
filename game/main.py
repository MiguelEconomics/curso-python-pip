print("""
Hi there! Let's play Rock 💥 / Paper 🧻 / Scissors ❌

Please type just the first letter of your choice and press Enter (lowercase or uppercase is ok).

R - Rock
P - Paper
S - Scissors

Note: In all fairness, please note that your input will be covered
""")

list = ["R", "P", "S"]

player1 = input("Player 1, please introduce your name: ")
player2 = input("Player 2, please introduce your name: ")

score1 = 0
score2 = 0

from getpass import getpass as input

print("Let's start!!!")
while True:  
  print("")
  
  option1 = input(f"{player1} what's your option? ").upper()
  option2 = input(f"{player2} your turn ").upper()

  # Game development
  if option1 == "R":
    if option2 == "R":
      print("Draw! 🤷‍♂️")
    elif option2 == "P":
      print("Paper beats Rock, " + player2 + " wins 😀")
      score2 += 1
    elif option2 == "S":
      print("Rock beats Scissors, " + player1 + " wins 😺")
      score1 += 1
    else:
      print(f"Sorry {player2} I could not recognize your input")
    
        
  elif option1 == "P":
    if option2 == "R":
      print("Paper beats Rock, " + player1 + " wins 😺")
      score1 += 1
    elif option2 == "P":
      print("Draw!")
    elif option2 == "S":
      print("Scissors beats paper, " + player2 + " wins 😀")
      score2 += 1
    else:
      print(f"Sorry {player2} I could not recognize your input")
        
  elif option1 == "S":
    if option2 == "R":
      print("Rock beats Scissors, " + player2 + " wins 😀")
      score2 += 1
    elif option2 == "P":
      print("Scissors beats Paper, " + player1 + " wins 😺")
      score1 += 1
    elif option2 == "S":
      print("Draw!")
    else:
      print(f"Sorry {player2} I could not recognize your input")
    
  else:
    print(f"Sorry {player1} I could not recognize your input. Please introduce the first letter of your option.")
  print(f"😺 {player1}'s score: {score1}  VS 😀 {player2}'s score: {score2} ")    
  if score1 == 3:
    print(f"Congrats {player1}! You won 🎉😸🎉")
    break
  if score2 == 3:
    print(f"Congrats {player2}! You won 🎉😁🎉")
    break    
  continue
exit()
  
  

