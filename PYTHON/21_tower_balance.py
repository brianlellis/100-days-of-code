import re
from data.data_21_tower_balance import puzzle_input

# prog_split = puzzle_input[0].split('->')
# num = prog_split[0].split()[1]
# num_key = int(re.sub(r'[\(\)]','',num))
# print(num_key)

# if len(prog_split) > 1:
#   print(re.sub(r'\s','',prog_split[1]).split(','))

# prog_split = puzzle_input[1].split('->')
# num = prog_split[0].split()[1]
# num_key = int(re.sub(r'[\(\)]','',num))
# print(num_key)

class TowerEval:
  def __init__(self, arr):
    self.input             = arr
    self.flat_map          = {}
    self.iso_progs         = {}
    self.big_progs         = {}
    self.big_prog_sub_list = []
    self.big_prog_tree     = False
    self.bottom_prog       = False
    self.uncommon_weight   = []
    self.evalRecords()
    self.bottomProg()
    self.bigMapper()

  def evalRecords(self):
    for val in self.input:
      prog_split = val.split('->')
      val_split  = prog_split[0].split()
      num_key    = int(re.sub(r'[\(\)]','',val_split[1])) # num_key is weight which I wrongly assumed sorts bottom block

      if len(prog_split) > 1:
        # Programs Being Held
        sub_list = re.sub(r'\s','',prog_split[1]).split(',')
        self.big_prog_sub_list += sub_list
        self.big_progs[val_split[0]] = {
          'iso_map'   : sub_list,
          'wght'      : num_key,
          'sub_progs' : {}
        }
      else:
        self.iso_progs[val_split[0]] = num_key

  def bottomProg(self):
    for prog_key in self.big_progs:
      if prog_key not in self.big_prog_sub_list:
        self.bottom_prog   = prog_key
        self.big_prog_tree = self.big_progs[prog_key]
        break

  def bigMapper(self, prog_key=False, prog_part=False):
    # Go bottomUp through the iso_maps, checking bigProgs 1st then isoProgs to determine tree structure
    # self.
    prog_key  = prog_key if prog_key else self.bottom_prog
    prog_part = prog_part if prog_part else self.big_prog_tree
    for sub_prog_key in self.big_progs[prog_key]['iso_map']:
      if sub_prog_key in self.big_progs:
        prog_part['sub_progs'][sub_prog_key] = self.big_progs[sub_prog_key]

        if len(prog_part['sub_progs'][sub_prog_key]['iso_map']) > 0:
          self.bigMapper(sub_prog_key, prog_part['sub_progs'][sub_prog_key])
      else:
        prog_part['sub_progs'][sub_prog_key] = self.iso_progs[sub_prog_key]

  # WEIGHT BALANCE IS WAY OFF ;/ ... no idea atm
  def weightBalanceCheck(self, prog_part):
    iso_map = prog_part['iso_map']
    wghts   = { iso_map[i]: False for i in range(0, len(iso_map)) }
    for prog_key in wghts:
      wghts[prog_key] = self.weightEval(prog_part['sub_progs'][prog_key])

    print(wghts)


  def weightEval(self, prog_part, wght=0):
    wght+=prog_part['wght']
    # return wght
    for sub_prog_key in prog_part['sub_progs']:
      if sub_prog_key in self.big_progs:
        wght+=prog_part['sub_progs'][sub_prog_key]['wght']
        self.weightEval(prog_part['sub_progs'][sub_prog_key], wght)
      else:
        wght+=(prog_part['sub_progs'][sub_prog_key] * len(prog_part['sub_progs']))

    return wght



part1 = TowerEval(puzzle_input)
part1.weightBalanceCheck(part1.big_prog_tree)
# print(part1.bottom_prog)
# print(part1.big_prog_tree)

# print('===== ISOLATED PROGS =====')
# print(part1.iso_progs)
# print('===== BUCKET/BIG PROGS =====')
# print(part1.big_progs)


