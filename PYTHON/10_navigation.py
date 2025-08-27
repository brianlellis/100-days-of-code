from data.data_10_navigation import puzzle_input

# Santa is delivering presents to an infinite two-dimensional grid of houses.
# He begins by delivering a present to the house at his starting location, and then 
# an elf at the North Pole calls him via radio and tells him where to move next. Moves 
# are always exactly one house to the north (^), south (v), east (>), or west (<). 
# After each move, he delivers another present to the house at his new location.

# However, the elf back at the north pole has had a little too much eggnog, and so his 
# directions are a little off, and Santa ends up visiting some houses more than once. 
# How many houses receive at least one present?

# PART 1
def flyEval(puzzle_input):
  compass  = [0,0] # N+/S- E+/W-
  houses   = ["D0D0"]
  presents = 1 # Starting house

  for direction in puzzle_input: 
    if direction == "^" or direction == "v": # N/S
      compass[0] -= -1 if direction == "^" else 1 
    else: # E/W
      compass[1] -= -1 if direction == ">" else 1

    string_ints = [f'D{str(int)}' for int in compass] # 0 is creating empty str so prefix req
    house_visit = "".join(string_ints)
    if house_visit not in houses:
      houses.append(house_visit)
      presents += 1

  print("PART 1:")
  print(presents) # 2572

flyEval(puzzle_input)

# PART 2
# The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, 
# to deliver presents with him.

# Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), 
# then take turns moving based on instructions from the elf, who is eggnoggedly reading from the 
# same script as the previous year.
def flyEval2(puzzle_input):
  compasses = [[0,0], [0,0]] # [ N+/S- E+/W- ] 
  houses    = ["D0D0"]
  presents  = 1 # Starting house

  for idx, direction in enumerate(puzzle_input):
    compass = 1 if idx % 2 == 0 else 0
    if direction == "^" or direction == "v": # N/S
      compasses[ compass ][0] -= -1 if direction == "^" else 1 
    else: # E/W
      compasses[ compass ][1] -= -1 if direction == ">" else 1

    string_ints = [f'D{str(int)}' for int in compasses[ compass ]] # 0 is creating empty str so prefix req
    house_visit = "".join(string_ints)
    if house_visit not in houses:
      houses.append(house_visit)
      presents += 1

  print("PART 2:")
  print(presents) # 2631

flyEval2(puzzle_input)
