import sys
import random

def evalChoice(user, comp):
  choice = ('Rock','Paper','Scissors')

  if user == comp:
    print(f"It's a tie!!! Play again\nBoth chose {choice[user]}")
    return True
  elif (user == 0 and comp == 2) or (user > comp and user != 2):
    print(f'User wins! \n{choice[user]} beats {choice[comp]}')
  else:
    print(f'User loses :(\n{choice[comp]} beats {choice[user]}')

  return False

def playGame():
  user   = int( input("Choose (0)Rock, (1)Paper, (2)Scissors... ") )
  comp   = random.randint(0,2)

  if ( evalChoice(user, comp) ): playGame()

  again = input("\n\nWould you like to play again (y/n)? ")
  if (again == "y"): 
    playGame()
  else:
    sys.exit()

print("Welcome to Rock, Paper Scissors")
print("\n 0: Rock, 1: Paper, 2: Scissors")
playGame()
