
"""

Problem
--------------

- Input: list of integers
- Output: list of strings
  - each element contains a number string or range between two numbers
  - "2", "4->7"


Examples
--------------

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"


Algorithm
--------------

1. Create variables: start_of_range, end_of_range, result
2. Loop through `nums`
  - if start_of_range is None: set start_of_range to current num
  - if num[idx + 1] - nums[idx] = 1 then set end_of_range to idx + 1
    -else:
      -if "end_of_range" is not none
        - append to `result` - "start_of_range->end_of_range"
      - if "end_of_range" is none
        - append to `result` - "start_of_range"
      - else: set start_of_range to None, end_of_range to None
3. return result

"""
from typing import List
class Solution:
  def summaryRanges(self, nums: List[int]) -> List[str]:
    start_of_range = None
    end_of_range = None
    result = []

    # edge cases
    if (len(nums) == 1):
      result.append(f"{nums[0]}")

    for idx in range(len(nums) - 1):
      if start_of_range is None:
        start_of_range = nums[idx]

      if nums[idx + 1] - nums[idx] == 1:
        end_of_range = nums[idx + 1]
      else:
        if end_of_range is not None:
          result.append(f"{start_of_range}->{end_of_range}")
        elif end_of_range is None:
          result.append(f"{start_of_range}")

        start_of_range = None
        end_of_range = None

      # Check for end of list
      if idx + 2 > len(nums) -1 and start_of_range is not None and end_of_range is not None:
        result.append(f"{start_of_range}->{end_of_range}")
      elif idx + 2 > len(nums) - 1 and start_of_range is None and end_of_range is None:
        result.append(f"{nums[idx + 1]}")

    return result


sol = Solution()
# print(sol.summaryRanges([0,1,2,4,5,7])) # ["0->2","4->5","7"]
# print(sol.summaryRanges([0,2,3,4,6,8,9])) # ["0","2->4","6","8->9"]
print(sol.summaryRanges([-1])) # ["-1"]
