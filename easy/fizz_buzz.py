
"""
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Input: integer
Output: array of strings

Algorithm:
  - Create a `results` variable
  - Loop from 1 to `n` and apply the logic given above based on above
    - i.e. if i is divisible by 3, answer[i] == "Fizz"
    - else the current index is appended
  - Return results
"""

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
      results = []
      for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
          results.append("FizzBuzz")
        elif i % 3 == 0:
          results.append("Fizz")
        elif i % 5 == 0:
          results.append("Buzz")
        else:
          results.append(str(i))
      return results


sol = Solution()
print(sol.fizzBuzz(5)) # ["1","2","Fizz","4","Buzz"]
print(sol.fizzBuzz(3)) # ["1","2","Fizz"]
