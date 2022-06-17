"""
  ================== WHEN TO USE EACH SORTING ALGORITHM ==================
  - Selection
    1.  When the list is small. As the time complexity of selection sort is O(N2) which makes it inefficient for a large list.
    2.  When memory space is limited because it makes the minimum possible number of swaps during sorting.

  - Bubble
    1.  It works well with large datasets where the items are almost sorted because it takes only one iteration to detect
        whether the list is sorted or not. But if the list is unsorted to a large extend then this algorithm holds good for small datasets or lists.
    2.  This algorithm is fastest on an extremely small or nearly sorted set of data

  - Insertion
    1.  If the data is nearly sorted or when the list is small as it has a complexity of O(N2) and if the list is sorted a minimum number 
        of elements will slide over to insert the element at it’s correct location.
    2.  This algorithm is stable and it has fast running case when the list is nearly sorted.
    3.  The usage of memory is a constraint as it has space complexity of O(1).

  - Merge
    1.  Merge sort is used when the data structure doesn’t support random access since it works with pure sequential access that 
        is forward iterators, rather than random access iterators.
    2.  It is widely used for external sorting, where random access can be very, very expensive compared to sequential access.
    3.  It is used where it is known that the data is similar data.
    4.  Merge sort is fast in the case of a linked list.
    5.  It is used in the case of a linked list as in linked list for accessing any data at some index we need to 
        traverse from the head to that index and merge sort accesses data sequentially and the need of random access is low.
    6.  The main advantage of the merge sort is its stability, the elements compared equally retain their original order.

  - Quick
    1.  Quick sort is fastest, but it is not always O(N*log N), as there are worst cases where it becomes O(N2).
    2.  Quicksort is probably more effective for datasets that fit in memory. For larger data sets it proves to be 
        inefficient so algorithms like merge sort are preferred in that case.
    3.  Quick Sort in is an in-place sort (i.e. it doesn’t require any extra storage) so it is appropriate to use it for arrays.
"""
arr = [ 2, 10, 23, 1, 57, 33, 35, 65, 88, 1001, 11, 97 ]

# ==== BUBBLE SORT ( slower O(N^2) )
def bubbleSort(arr):
  arr_len = len(arr)
  tmp     = arr.copy()
  
  for i in range(arr_len):
    for j in range(0, arr_len-i-1):
      nxt = j+1
      if tmp[j] > tmp[nxt]:
        tmp[j], tmp[nxt] = tmp[nxt], tmp[j]

  return tmp

print(f'Sorted array is: {bubbleSort(arr)}')

# ==== SELECTION SORT ( faster O(N^2) )
def selectionSort(arr):
  arr_len = len(arr)
  tmp     = arr.copy()

  for step in range(arr_len):
    min_idx = step

    for i in range(step + 1, arr_len):
      if tmp[i] < tmp[min_idx]:
        min_idx = i
     
    (tmp[step], tmp[min_idx]) = (tmp[min_idx], tmp[step])

  return tmp

print(f'Sorted array is: {selectionSort(arr)}')

# ==== BUCKET SORT ( faster smaller collections O(N+K) )
def bucket_sort(input_list):
  def insertion_sort(bucket):
    for i in range (1, len (bucket)):
      var = bucket[i]
      j = i - 1
      while (j >= 0 and var < bucket[j]):
        bucket[j + 1] = bucket[j]
        j = j - 1
      bucket[j + 1] = var
  # END fn()
          
  max_value = max(input_list)
  size      = max_value/len(input_list)

  buckets_list= []
  for x in range(len(input_list)):
    buckets_list.append([]) 

  # Put list elements into different buckets based on the size
  for i in range(len(input_list)):
    j = int (input_list[i] / size)
    if j != len (input_list):
      buckets_list[j].append(input_list[i])
    else:
      buckets_list[len(input_list) - 1].append(input_list[i])

  # Sort elements within the buckets using Insertion Sort
  for z in range(len(input_list)):
    insertion_sort(buckets_list[z])
          
  # Concatenate buckets with sorted elements into a single list
  final_output = []
  for x in range(len (input_list)):
    final_output = final_output + buckets_list[x]

  return final_output

print(f'Sorted array is: {bucket_sort(arr)}')

# ==== MERGE SORT ( faster smaller collections O(N+K) )
def mergeSort(arr):
  arr_len = len(arr)

  if arr_len > 1:
    mid = arr_len//2 # Finding the mid of the array
    L = arr[:mid]     # Dividing the array elements
    R = arr[mid:]     # into 2 halves
    mergeSort(L)      # Sorting the first half
    mergeSort(R)      # Sorting the second half
    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
      if L[i] < R[j]:
        arr[k] = L[i]
        i += 1
      else:
        arr[k] = R[j]
        j += 1
      k += 1

    # Checking if any element was left
    while i < len(L):
      arr[k] = L[i]
      i += 1
      k += 1

    while j < len(R):
      arr[k] = R[j]
      j += 1
      k += 1
    
    return arr

print(f'Sorted array is: {mergeSort(arr.copy())}')


# ==== QUICK SORT ( faster smaller collections O(N+K) )
def quicksort(l, r, nums):
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
    quicksort(l, pi-1, nums)  # Recursively sorting the left values
    quicksort(pi+1, r, nums)  # Recursively sorting the right values
  return nums

print(f'Sorted array is: {quicksort(0, len(arr)-1, arr.copy())}')