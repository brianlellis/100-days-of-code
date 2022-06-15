import sys
import random

def evalChoice(user, comp):
  choice = ('Rock','Paper','Scissors')

  if (user == 0 and comp == 2) or (user > comp and user != 2):
    print("User wins!")
    print(f'{choice[user]} beats {choice[comp]}')
    return False
  elif user == comp:
    print("It's a tie!!! Play again")
    print(f'Both chose {choice[user]}')
    return True
  else:
    print("User loses :(")
    print(f'{choice[comp]} beats {choice[user]}')
    return False

def playGame():
  user   = input("Choose (0)Rock, (1)Paper, (2)Scissors... ")
  comp   = random.randint(0,2)

  if ( evalChoice( int(user), int(comp) ) ): playGame()

  again = input("\n\nWould you like to play again (y/n)? ")
  if (again == "y"): 
    playGame()
  else:
    sys.exit()

print("Welcome to Rock, Paper Scissors")
print("\n 0: Rock, 1: Paper, 2: Scissors")
playGame()

