puzzle_input = [0,5,10,0,11,14,13,4,11,8,8,7,1,4,12,11]

class InfiniteCheck:
  def __init__(self, arr):
    self.input         = arr
    self.input_len     = len(arr)
    self.distributions = []
    self.invocations   = self.loop_cnt = 0
    self.evalInfinite()

  def maxIdx(self):
    # print(f'START INPUT: {self.input}')
    max_val = self.input[0]
    max_idx = 0
    for idx in range(0,self.input_len):
      if max_val < self.input[idx]:
        # print('Changing Max')
        max_val = self.input[idx]
        max_idx = idx

    self.input[max_idx] = 0
    max_idx+=1 # Offset to start at correct distribution idx
    return max_val, max_idx

  def redistribute(self, start_idx, redis_val):
    self.invocations+=1

    while redis_val > 0:
      if start_idx >= self.input_len: start_idx = 0
      self.input[start_idx] += 1
      start_idx+=1
      redis_val-=1
      # print(f'INPUT: {self.input} --- REDIS VALUE: {redis_val}')

    distribution = ''.join([str(i) for i in self.input])
    if distribution in self.distributions:
      # loops between remove the last invocation hence +1
      # or you could (self.invocations-1) to get correct loop count
      self.loop_cnt = self.invocations - (self.distributions.index(distribution)+1)
      return False
    else:
      self.distributions.append(distribution)
      return True

  def evalInfinite(self):
    max_val, max_idx = self.maxIdx()
    times = 0
    while self.redistribute(max_idx, max_val):
      max_val, max_idx = self.maxIdx()
      times+=1

test_input = [0,2,7,0]
test1 = InfiniteCheck(test_input)
print(test1.invocations)
print(test1.loop_cnt)

part1 = InfiniteCheck(puzzle_input)
print(part1.invocations)
print(part1.loop_cnt)

# PART 2
# Out of curiosity, the debugger would also like to know the size of the loop: 
# starting from a state that has already been seen, how many block redistribution 
# cycles must be performed before that same state is seen again?

# In the example above, 2 4 1 2 is seen again after four cycles, and so the answer in that example would be 4.
