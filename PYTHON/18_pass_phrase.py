from data.data_18_pass_phrase import puzzle_input

# A new system policy has been put in place that requires all accounts to use a passphrase instead
# of simply a password. A passphrase consists of a series of words (lowercase letters) separated by spaces.

# To ensure security, a valid passphrase must contain no duplicate words.
# For example:
# aa bb cc dd ee is valid.
# aa bb cc dd aa is not valid - the word aa appears more than once.
# aa bb cc dd aaa is valid - aa and aaa count as different words.

class PhraseCheck:
  def __init__(self, arr_sets, anaMatch=False):
    self.valid_total = 0
    self.ana_match   = anaMatch
    self.phraseValidSum(arr_sets)

  def phraseValidSum(self, arr_sets):
    valid_str = 0
    for arr in arr_sets:
      if self.ana_match:
        words = sorted(list(map( lambda word: ''.join(sorted(word)), arr.split() )))
        if self.matchCheck( sorted(words) ): self.valid_total+=1
      elif self.matchCheck( sorted(arr.split()) ): 
        self.valid_total+=1

  def matchCheck(self, arr):
    for idx in range(0, len(arr)-1):
      if arr[idx] == arr[idx+1]: return False
    return True


test_input = ["aa bb cc dd ee", "aa bb cc dd aa", "aa bb cc dd aaa"] # 2 valid
test1 = PhraseCheck(test_input)
print(test1.valid_total)

part1 = PhraseCheck(puzzle_input)
print(part1.valid_total)

# PART 2
# For added security, yet another system policy has been put in place. Now, a valid passphrase must 
# contain no two words that are anagrams of each other - that is, a passphrase is invalid if any word's 
# letters can be rearranged to form any other word in the passphrase.

# For example:
# abcde fghij is a valid passphrase.
# abcde xyz ecdab is not valid - the letters from the third word can be rearranged to form the first word.
# a ab abc abd abf abj is a valid passphrase, because all letters need to be used when forming another word.
# iiii oiii ooii oooi oooo is valid.
# oiii ioii iioi iiio is not valid - any of these words can be rearranged to form any other word.
part2 = PhraseCheck(puzzle_input, True)
print(part2.valid_total)

