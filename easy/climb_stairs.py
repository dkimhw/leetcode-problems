
"""

Input: integer (n steps)
Output: integer - # of distinct ways to climb stairs
  - you can take 1 or 2 steps

Test Cases:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

Algorithm:
- Create a helper recurser function
- Helper recursion function
  - Input: `n` and `current_steps` (counts the number of distinct steps)
  - Output: return 1 if n == 3 else 0
  - Break condition:
    - if current_step == n return 1
    - if current_step > n return 0
  - Recursion part:
    - for each action (1 step or 2 steps)
      - call helper recursion function passing in current steps and n
        - current steps + current action step amount (1 or 2)
      - add up the return value as the functions finishes

"""


class Solution:
  def climbStairs(self, n: int) -> int:
    results = [0]
    def climb_stairs_recursion_helper(n: int, curr_steps: int):
      if n == curr_steps:
        results[0] += 1
        return 1
      if curr_steps > n:
        return 0

      for i in range(1, 3):
        climb_stairs_recursion_helper(n, curr_steps + i)

    climb_stairs_recursion_helper(n, 0)
    return results[0]

sol = Solution()
print(sol.climbStairs(2)) #2

sol = Solution()
print(sol.climbStairs(3)) #3
