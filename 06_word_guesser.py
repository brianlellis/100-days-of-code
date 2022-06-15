import random
import re
import sys

def playAgain(str):
  print(str)
  again = input("Play again (y/n)? ")
  return again == "y"

def wordGuesser():
  words = [
    'relaxation',   'unpleasant',   'thoughtful',
    'atmosphere',   'restaurant',   'excavation',
    'vegetation',   'goalkeeper',   'appreciate',
    'simplicity',   'commitment',   'indication',
    'provincial',   'leadership',   'continuous',
    'conference',   'confidence',   'particular',
    'correspond',   'relinquish',
  ]

  print("\n\nLet's begin Word Guesser!\n")
  word  = random.choice( words )
  answ  = ['_' for x in range( len(word) )]
  
  tries   = int( input("How many tries? ") )
  correct = 0
  guessed = []

  while tries > 0:
    if correct == len(word):
      if ( playAgain("You won!!!") ):
        wordGuesser()
      else:
        sys.exit()

    print( "".join(answ) )
    print(f"\nYou have {tries} left.\n\n")
    guess = input("Guess a letter A-Z... ")

    while guess in guessed:
      print("You already picked that, try another one.")
      guess = input("Guess a letter A-Z... ")

    guessed.append(guess)
    indices = [ i.start() for i in re.finditer(guess, word) ]
    if indices:
      for idx in indices:
        correct += 1
        answ[idx] = guess
    else:
      tries -= 1

  if ( playAgain("You lost :(") ):
    wordGuesser()
  else:
    sys.exit()

wordGuesser()
