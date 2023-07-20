"""
https://leetcode.com/problems/intersection-of-two-arrays/submissions/
Problem
------------------

Input: two arrs `nums1` & `nums2`
Output: array
  - this array cotains the elements that appear in both input arrays
  - contains only unique elements
Notes:
  - the result can be in any order


Examples
------------------
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.


The question here is can we do better than O(mn)

O(n log n) + O(m log m) + O(m)

[1, 1, 2, 2], [2, 2]

Algorithm
---------------
1. Sort nums1 & nums2
2. Create a result - assign empty set
3. Maintain two counters (i, j)
4. Loop through nums1
  - if nums1[i] == nums[j] --> move up both i and j by 1
  - if nums1[i] != nums[j] --> move up i by 1
5. Return result


Better Algorithm
-------------------
1. Convert both to sets
2. Loop over nums1 set
  - check if nums1 element is in nums2 set
  - this is O(1) operation

O(2m + n) --> O(m + n)

"""

from typing import List

class Solution1:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    result = set()
    nums1_idx = 0
    nums2_idx = 0

    # Sort
    nums1.sort()
    nums2.sort()

    while nums1_idx < len(nums1) and nums2_idx < len(nums2):
      print(nums2_idx)
      if (nums1[nums1_idx] == nums2[nums2_idx]):
        result.add(nums1[nums1_idx])
        nums1_idx += 1
        nums2_idx += 1
      elif nums1[nums1_idx] > nums2[nums2_idx]:
        nums2_idx += 1
      else:
        nums1_idx += 1

    return list(result)


class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    set1 = set(nums1)
    set2 = set(nums2)
    result = []

    for el in set1:
      if el in set2:
        result.append(el)

    return result

sol = Solution()
# print(sol.intersection([1,2,2,1], [2,2]))
# print(sol.intersection([4,9,5], [9,4,9,8,4]))
print(sol.intersection([1,2], [1,1]))
