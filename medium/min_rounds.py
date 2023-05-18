"""

https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

Problem
--------------------

Input: Array of integers
  - each element (tasks[i]) represents the difficulty of each task
  - 2 > 1 for example
Output: integer
  - return the min rounds required to complete all tasks
Notes:
  - return -1 if it is not possible to complete all tasks
  - limitations**
    - you can only complete 2 or 3 tasks of the same difficulty level


Examples
--------------------

Input: tasks = [2,2,3,3,2,4,4,4,4,4]
Output: 4
Explanation: To complete all the tasks, a possible plan is:
- In the first round, you complete 3 tasks of difficulty level 2.
- In the second round, you complete 2 tasks of difficulty level 3.
- In the third round, you complete 3 tasks of difficulty level 4.
- In the fourth round, you complete 2 tasks of difficulty level 4.
It can be shown that all the tasks cannot be completed in fewer than 4 rounds, so the answer is 4.

Input: tasks = [2,3,3]
Output: -1
Explanation: There is only 1 task of difficulty level 2, but in each round, you can only complete either 2 or 3 tasks of the same difficulty level. Hence, you cannot complete all the tasks, and the answer is -1.


Algorithms Attempt:
1. create a map variable & results variable
2. loop through `tasks` and count the tasks using the task difficulty value as the key
3. loop through the map variable
  - for each k-v:
    - check if it can be grouped into 2 or 3* (Helper)
      - increment results by each group
    - if it cannot (returns -1 from the helper function)
      - return -1
4. return results

Helper (counting groups)
- So it can be grouped by 2 or 3
- I think recursion will be helpful here
  - base case
    - if <= 0, return
  - recursion step
    - recursion(currVal - 2)
    - recursion(currVal - 3)


Algorithm Attempt 2:
- Instead of recursing and finding all combinations of -2, -3 on each tree step:
- This is possible because we want to be greedy - take 3 at a time and account for cases where 3 doesn't quite fit
  - If map[el] == 1 then return - 1 (cannot break it apart)
  - If map[el] % 3 === 0 then add map[el] to results
- Scenarios where 3 doesn't fully divide
  - There is one left so something like 4
    -
  - There is two left so something like 5
"""
from typing import List
from collections import Counter

class SolutionAttempt:
  def group_by_two_and_three(self, num):
    def group_by_two_and_three_helper(num, result):
      if num == 0:
        # print("result: ", result)
        return result
      elif num < 0:
        return -1

      result += 1
      recurse1 = group_by_two_and_three_helper(num - 2, result)
      recurse2 = group_by_two_and_three_helper(num - 3, result)

      # print("recurse1: ", recurse1)
      # print("recurse2: ", recurse2)
      if (recurse1 == -1):
        return recurse2
      elif (recurse2 == -1):
        return recurse1
      else:
        return min(recurse1, recurse2)

    val = group_by_two_and_three_helper(num, 0)
    print("val", val)
    return val

  def minimumRounds(self, tasks: List[int]) -> int:
    result = 0
    map = Counter()

    # Count up the tasks by difficulty
    for el in tasks:
      map[el] += 1

    for _, val in map.items():
      min_group_cnt = self.group_by_two_and_three(val)

      if min_group_cnt == -1:
        return -1

      if min_group_cnt != -1:
        result += min_group_cnt
    return result

import math
class Solution:
  def minimumRounds(self, tasks: List[int]) -> int:
    result = 0
    map = Counter()

    # Count up the tasks by difficulty
    for el in tasks:
      map[el] += 1

    for _, val in map.items():
      if val == 1:
        return -1
      elif val % 3 == 0:
        result += int(val / 3)
      elif val % 3 == 1:
        result += (math.floor(val / 3) + 1)
      elif val % 3 == 2:
        result += (math.floor(val / 3) + 1)
    return result

# sol = Solution()
# print(sol.minimumRounds([2,2,3,3,2,4,4,4,4,4])) # 4
