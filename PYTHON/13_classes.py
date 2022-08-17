class Species:
  def __init__(self, name):
    self.species = name

    if name == 'Human':
      self.stats = self.statCreate([54,13,7,8])
    elif name == 'Troll':
      self.stats = self.statCreate([101,23,3,21])

  def statCreate(self, arr):
    return {
      "health"  : arr[0],
      "strength": arr[1],
      "magic"   : arr[2],
      "defense" : arr[3]
    }

class Equipment:
  def __init__(self):
    self.equipment = {
      "weapon": None,
      "helmet": None,
      "shirt" : None,
      "pants" : None,
      "shoes" : None,
      "acc1"  : None,
      "acc2"  : None,
    }

class Character(Equipment, Species):
  def __init__(self, name, species_name, char_type='Hero'):
    self.type = char_type
    self.name = name
    Equipment.__init__(self)
    Species.__init__(self, species_name)

  def charSummary(self):
    print("""
      ======= CHARACTER SUMMARY =======
      name     : {}
      species  : {}
      stats    : {}
      equipment: {}
    """.format(self.name, self.species, self.stats, self.equipment) )


hero1 = Character('Maxim','Human')
enemy = Character('Gorgon', 'Troll', 'Enemy')
hero1.charSummary()
enemy.charSummary()

