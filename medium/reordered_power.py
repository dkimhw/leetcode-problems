
"""

Input: integer `n`
Output: boolean
  - you can reorder any of the digits (or not if it's in power of 2 already)
    - since you can reorder any
    - we can't just take one digit at a time and move it around since I can move two digits at a time
  - return true if the reordered number is a power of two
  - cannot have a leading zero

Test Case:

Input: n = 1
Output: true

Input: n = 10
Output: false


Brute force O(2^n):
1. Check if input is order of 2 - return true
  - divide n by 2 until 0 and return false if % 2 != 0
2. Else:
  - generate all variations possible from the input digits
3. Then for each check if input is order of 2


Different approach - not sure if it's correct:
1. Catalog the digits in a dict (i.e. there are three ones in `n`)
2. Compare this to possible 2^n
3. Only compare the 2^n that has the same # of digits; if # of digits becomes bigger stop checking possible 2^n
4. Check the digits are the same then return ture
5. For all other cases: return false
"""

from collections import Counter

# Brute force
class Solution:
  def reorderedPowerOf2(self, n: int) -> bool:
    def possible_2n_vals(n):
      num_of_digits = len(list(str(n)))
      curr_cnt = 0
      curr_2n_num = 1
      curr_n = 0
      possible_2n_nums_to_check = []
      while curr_cnt <= num_of_digits:
        curr_2n_num = 2 ** curr_n
        curr_cnt = len(list(str(curr_2n_num)))
        # print(curr_2n_num)
        # print(num_of_digits)
        # print(curr_cnt)
        curr_n += 1
        if (curr_cnt == num_of_digits):
          dict_nums = Counter()
          for digit in list(str(curr_2n_num)):
            dict_nums[digit] += 1
          possible_2n_nums_to_check.append(dict_nums)

      return possible_2n_nums_to_check

    def compareDigits(curr_digits, comp_digits):
      for k, v in curr_digits.items():
        if k in comp_digits:
          if curr_digits[k] == comp_digits[k]:
            continue
          else:
            return False
        else:
          return False
      return True

    digits = Counter()
    for digit in list(str(n)):
      digits[digit] += 1

    possible_nums_to_check = possible_2n_vals(n)

    for num in possible_nums_to_check:
      if compareDigits(digits, num):
        return True
    return False

sol = Solution()
print(sol.reorderedPowerOf2(1))

# result = 1
# for i in range(50):
#   result *= 2
#   print(result)
