import math
from data.data_17_spreadsheet import puzzle_input

# As you walk through the door, a glowing humanoid shape yells in your direction. 
# "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - 
# if we take another millisecond, we'll have to display an hourglass cursor!"

# The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process 
# is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine
# the difference between the largest value and the smallest value; the checksum is the 
# sum of all of these differences.

# For example, given the following spreadsheet:
# 5 1 9 5
# 7 5 3
# 2 4 6 8
# The first row's largest and smallest values are 9 and 1, and their difference is 8.
# The second row's largest and smallest values are 7 and 3, and their difference is 4.
# The third row's difference is 6.
# In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

class CheckSum:
  def __init__(self, input_arr):
    self.total_sum = 0
    self.evalArr(input_arr)
    
  def maxDiff(self,input_val):
    min_val = max_val = input_val[0]
    for val in input_val:
      if val < min_val: min_val = val
      elif val > max_val: max_val = val

    self.total_sum += max_val-min_val

  def evalArr(self, input_val):
    for val in input_val: self.maxDiff(val)

test_input1 = [ [5,1,9,5], [7,5,3], [2,4,6,8] ]
test1 = CheckSum(test_input1)
print(test1.total_sum)

part1 = CheckSum(puzzle_input)
print(part1.total_sum)

# PART 2
# "Based on what we're seeing, it looks like all the User wanted is some information about the evenly 
# divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation 
# - most of us specialize in bitwise operations."

# It sounds like the goal is to find the only two numbers in each row where one evenly divides the other 
# - that is, where the result of the division operation is a whole number. They would like you to find 
# those numbers on each line, divide them, and add up each line's result.

class WholeNumberSum:
  def __init__(self, input_arr):
    self.total_sum = 0
    self.evalArr(input_arr)
    
  def isWhole(self,input_val):
    return ( input_val - int(input_val) ) == 0

  # ASCENDING ORDER FORMULA
  def quicksort(self, arr):
    return self.eval_quicksort(0, len(arr)-1, arr.copy())

  def eval_quicksort(self, l, r, nums):
    def partition(l, r, nums):
      # Last element will be the pivot and the first element the pointer
      pivot, ptr = nums[r], l
      for i in range(l, r):
        if nums[i] <= pivot:
          # Swapping values smaller than the pivot to the front
          nums[i], nums[ptr] = nums[ptr], nums[i]
          ptr += 1
      # Finally swapping the last element with the pointer indexed number
      nums[ptr], nums[r] = nums[r], nums[ptr]
      return ptr
      # END fn()


    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
      return nums
    if l < r:
      pi = partition(l, r, nums)
      self.eval_quicksort(l, pi-1, nums)  # Recursively sorting the left values
      self.eval_quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums

  def evalArr(self, input_val):
    total_sum = 0
    
    for arr_set in input_val:
      last_half  = math.ceil(len(arr_set) / 2)
      first_half = last_half-1
      ranger1    = range(0,first_half+1)
      ranger2    = range(last_half,last_half+first_half+1)
      arr_sort   = self.quicksort(arr_set)

      for idx1 in ranger1:
        prev_sum = self.total_sum

        for idx2 in ranger2:
          calc = arr_sort[idx2] / arr_sort[idx1]
          if self.isWhole(calc):
            self.total_sum += int(calc)
            break

        if prev_sum < self.total_sum: break

print('======= PART 2 =======')
test_input2 = [ [5,9,2,8], [9,4,7,3], [3,8,6,5] ]
test2 = WholeNumberSum(test_input2)
print(test2.total_sum)

part2 = WholeNumberSum(puzzle_input)
print(part2.total_sum)
