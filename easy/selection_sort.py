
"""
Implement selection sort

Input: array of nums
Output: array of nums sorted in asc order

Algorithm:
- Create variable curr_idx
- Repeat:
  - Loop through the array
    - Find the lowest number's from elements > curr_idx
  - At the end of the loop move that number to curr_idx location
    - Insert the lowest number at the curr_idx + 1
    - Remove the lowest number at lowest index
  - Break condition:
    - if curr_idx = len(nums) - 1
"""

from typing import List

class Solution:
  def selectionSort(self, nums: List[int]) -> List[int]:
    curr_idx = 0
    while curr_idx < len(nums):
      lowest_num = curr_idx
      for i in range(curr_idx, len(nums)):
        if nums[i] < nums[lowest_num]:
          lowest_num = i

      # swap
      if lowest_num != curr_idx:
        low_num = nums[lowest_num]
        nums.pop(lowest_num)
        nums.insert(curr_idx, low_num)
        curr_idx += 1

      return nums

sol = Solution()
print(sol.selectionSort([2, 1, 3]))

"""
Alt:

function selectionSort(array) {
  const length = array.length;
  for(let i = 0; i < length; i++){
    let min = i;
    let temp = array[i];
    for(let j = i+1; j < length; j++){
      if (array[j] < array[min]){
        min = j;
      }
    }
    array[i] = array[min];
    array[min] = temp;
  }
  return array;
}
"""
