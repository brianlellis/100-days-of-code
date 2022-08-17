# UNIFINISHED --- NOT GREAT AT PLOT POINTING GEOMETRY :(
puzzle_input = ("L2","L3","L3","L4","R1","R2","L3","R3","R3","L1","L3","R2","R3","L3","R4","R3","R3","L1","L4","R4","L2","R5","R1","L5","R1","R3","L5","R2","L2","R2","R1","L1","L3","L3","R4","R5","R4","L1","L189","L2","R2","L5","R5","R45","L3","R4","R77","L1","R1","R194","R2","L5","L3","L2","L1","R5","L3","L3","L5","L5","L5","R2","L1","L2","L3","R2","R5","R4","L2","R3","R5","L2","L2","R3","L3","L2","L1","L3","R5","R4","R3","R2","L1","R2","L5","R4","L5","L4","R4","L2","R5","L3","L2","R4","L1","L2","R2","R3","L2","L5","R1","R1","R3","R4","R1","R2","R4","R5","L3","L5","L3","L3","R5","R4","R1","L3","R1","L3","R3","R3","R3","L1","R3","R4","L5","L3","L1","L5","L4","R4","R1","L4","R3","R3","R5","R4","R3","R3","L1","L2","R1","L4","L4","L3","L4","L3","L5","R2","R4","L2")

class Compass:
  def __init__(self):
    self.start_dir = "N"
    self.cur_dir   = self.start_dir
    self.steps     = {
      "N": 0,
      "E": 0,
      "W": 0,
      "S": 0
    }

  def turn(self,direction):
    if self.cur_dir == "N":
      self.cur_dir = "W" if direction == "L" else "E"
    elif self.cur_dir == "E":
      self.cur_dir = "N" if direction == "L" else "S"
    elif self.cur_dir == "S":
      self.cur_dir = "E" if direction == "L" else "W"
    elif self.cur_dir == "W":
      self.cur_dir = "N" if direction == "L" else "S"

  def calcStep(self, steps):
    if self.cur_dir == "N" or self.cur_dir == "E":
      self.steps[self.cur_dir] += int(steps)
    elif self.cur_dir == "W" or self.cur_dir == "S":
      self.steps[self.cur_dir] -= int(steps)

  def walk(self, move):
    self.turn(move[0])
    self.calcStep(move[1:])

  def plotPoint(self):
    vert = self.steps["N"] + self.steps["S"]
    hori = self.steps["E"] + self.steps["W"]
    print(f'Plot Point === X: {hori}, Y: {vert}')
    print(self.steps)

  def parseDirections(self, directions):
    for move in directions: self.walk(move) 
    self.plotPoint()



# PART 1
# You're airdropped near Easter Bunny Headquarters in a city somewhere. 
# Near, unfortunately, is as close as you can get - the instructions on the 
# Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

# The Document indicates that you should start at the given coordinates (where you just landed) and face North. 
# Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, 
# then walk forward the given number of blocks, ending at a new intersection.

# How many blocks away is Easter Bunny HQ?

# test_input = ("R5", "L5", "R5", "R3")
# test1 = Compass()
# test1.parseDirections(test_input)

part1 = Compass()
part1.parseDirections(puzzle_input)
