"""
In this brute force approach we take all possible step combinations i.e. 1 and 2, at every step.
At every step we are calling the function climbStairs for step 1 and 2
, and return the sum of returned values of both functions.

climbStairs(i,n) = (i+1,n) + climbStairs(i+2,n)

where i defines the current step and nnn defines the destination step.


public class Solution {
    public int climbStairs(int n) {
        return climb_Stairs(0, n);
    }
    public int climb_Stairs(int i, int n) {
        if (i > n) {
            return 0;
        }
        if (i == n) {
            return 1;
        }
        return climb_Stairs(i + 1, n) + climb_Stairs(i + 2, n);
    }
}
"""

from typing import List

class Solution:
  def climbStairs(self, n: int) -> int:
    def climb_stairs_helper(n: int, curr_steps: int, memo: List) -> int:
      if n == curr_steps:
        return 1
      if curr_steps > n:
        return 0
      if memo[curr_steps] > 0:
        return memo[curr_steps]

      memo[curr_steps] = climb_stairs_helper(n, curr_steps + 1, memo) + climb_stairs_helper(n, curr_steps + 2, memo)
      return memo[curr_steps]

    memo = [0] * n
    return climb_stairs_helper(n, 0, memo)


sol = Solution()
print(sol.climbStairs(2)) #2

sol = Solution()
print(sol.climbStairs(3)) #3
