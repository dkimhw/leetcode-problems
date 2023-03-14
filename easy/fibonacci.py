
"""
Write a recursion function for returning a fibonnaci seq
"""

class Solution:
  def fibonacci(self, n):
    # Base case
    if n == 1:
      return 0
    elif n == 2:
      return 1

    return self.fibonacci(n - 1) + self.fibonacci(n - 2)


sol = Solution()
print(sol.fibonacci(1)) # 0
print(sol.fibonacci(2)) # 1
print(sol.fibonacci(5)) # 3
print(sol.fibonacci(7)) # 8
