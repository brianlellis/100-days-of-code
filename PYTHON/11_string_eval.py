import re
from data.data_11_string_eval import puzzle_input

# Santa needs help figuring out which strings in his text file are naughty or nice.

# A nice string is one with all of the following properties:

# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
def strEval(string):
  not_pattern   = re.compile(r'ab|cd|pq|xy', re.I)
  not_contained = bool( not_pattern.search(string) )

  rep_pattern   = re.compile(r'([a-z])\1{1}', re.I)
  rep_contained = bool( rep_pattern.search(string) )

  vow_pattern   = re.compile(r'[aeiou]', re.I)
  vow_contained = vow_pattern.findall(string)
  
  return not not_contained and rep_contained and len(vow_contained) >= 3

# Realizing the error of his ways, Santa has switched to a better model of determining whether a string 
# is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

# Now, a nice string is one with all of the following properties:

# It contains a pair of any two letters that appears at least twice in the string without overlapping, like 
# xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, 
# abcdefeghi (efe), or even aaa.

def strEval2(string):
  norep_contained = re.search('([a-z][a-z]).*\\1',string)==None
  rep_contained   = re.search('([a-z]).\\1',string)==None
  
  return not norep_contained and not rep_contained
 
def part1(puzzle_input):
  nice_cnt = 0
  for string in puzzle_input:
    if strEval(string): nice_cnt += 1

  return nice_cnt

print("Part 1:")
print( part1(puzzle_input) )

def part2(puzzle_input):
  nice_cnt = 0
  for string in puzzle_input:
    if strEval2(string): nice_cnt += 1

  return nice_cnt

print("Part 2:")
print( part2(puzzle_input) )
