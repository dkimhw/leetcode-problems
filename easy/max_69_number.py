
"""

https://leetcode.com/problems/maximum-69-number/

Input: integer (consisting only of 6 and 9)
Output: integer
  - returns the maximum number possible from 6 and 9
  - you may switch at most one digt


Input: num = 9669
Output: 9969
Explanation:
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.

Algorithm:
- create a variable called max_num = `num`
- loop through the digits:
    - if the current digit is 6
      - change to 9 and take the max of current `max_num` and the changed number
- return max_num

9669

max_num = 9669
iteration 0: 9669
iteration 1: 9969 so take 9969
iteration 2: 9699 so still 9969
iteration 3: 9699

so 9969

"""

class Solution:
  def maximum69Number (self, num: int) -> int:
    max_num = num
    str_num = str(num)
    for idx in range(len(str_num)):
      if str_num[idx] == '6':
        left_digits = str_num[0:idx]
        right_digits = str_num[idx + 1:] if idx + 1 < len(str_num) else None
        print(idx)

        if right_digits != None:
          new_str_num = left_digits + '9' + right_digits
        else:
          new_str_num = left_digits + '9'
        max_num = max(int(new_str_num), max_num)


    return max_num

sol = Solution()
print(sol.maximum69Number(9669))
