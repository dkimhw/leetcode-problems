"""
Using recursion write a factorial function and not a loop
"""

class Solution:
  def factorial(self, n):
    # Base case:
    if n == 1:
      return 1

    return n * self.factorial(n - 1)


sol = Solution()
print(sol.factorial(5))
