
"""
https://leetcode.com/problems/container-with-most-water/

Input: list of integers (each element is height)
Output: integer
  - maximum area of water

Test Case

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

left = 0
right = 9
height = min(heights[left], heights[right]) = 1
width = right - left = 9

height * width = 9

left = 1
right = 9
height = min(heights[left], heights[right]) = 6
width = right - left = 8
area = 48

What is the intuition for incrementing left vs right?
  - Since each time you move the outer pointers in - you lose one width
  - So it's really only worthwhile to increment and check if the height is an improvement over the current height
  - keep the bigger of the two heights

[1,8,6,2,100,60,8,3,7]
- 8, 7 is the best in the beg
- Increment left, 6, 2 are not helpful
- 100 is definitely worth checking
  - then decrement right
  - untily we hit 60 which is worth checking again

[1,8,6,2,1,2,8,50,7]

[1,8,100,2,1,2,8,50,7]

Algorithm
- We have two pointers - left and right (0, len(n) - 1)
- We have max_area to keep track of current max area
- While left < right
  - if curr_max_area > max_area then reassign max_area
  - if left is >= right: decrement right
  - if left is < right: increment left
- return max_area
"""
from typing import List

class Solution:
  def maxArea(self, height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
      curr_max_area = min(height[left], height[right]) * (right - left)
      max_area = max(curr_max_area, max_area)
      if height[left] >= height[right]:
        right -= 1
      else:
        left += 1

    return max_area

sol = Solution()

print(sol.maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(sol.maxArea([1,8,6,2,100,60,8,3,7])) # 60
print(sol.maxArea([1,8,6,2,100, 1 ,60,8,3,7])) # 120
