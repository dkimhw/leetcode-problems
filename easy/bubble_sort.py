
"""
Implement a bubble sort function

Algorithm:
1. Set is_swapped = false
2. While true
  - loop through the array in pairs - comparing and swapping if the num1 > num2
  - if at the end of the loop nothing was swapped - break
3. return nums
"""

def bubbleSort(nums):
  is_swapped = False
  while True:
    for i in range(len(nums)):
      if i + 1 < len(nums):
        if nums[i] > nums[i + 1]:
          tmp = nums[i]
          nums[i] = nums[i + 1]
          nums[i + 1] = tmp
          is_swapped = True
    if not is_swapped:
      break
    is_swapped = False
  return nums

arr = [5, 1, 4, 2, 8]

print(bubbleSort(arr))
