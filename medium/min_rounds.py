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


Algorithms:
1. create a map variable & results variable
2. loop through `tasks` and count the tasks using the task difficulty value as the key
3. loop through the map variable
  - for each k-v:
    - check if it can be grouped into 2 or 3*
      - incrmeent results by each group
    - if it cannot
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

7 - 3, 3, 1 does not work, you need 3, 2, 2

"""

def group_by_two_and_three(num):
  def group_by_two_and_three_helper(num, result):
    if num == 0:
      # print("hello")
      # print(result, "result")
      return result
    elif num < 0:
      return -1

    # print("result", result)
    result += 1
    recurse1 = group_by_two_and_three_helper(num - 2, result)
    recurse2 = group_by_two_and_three_helper(num - 3, result)

    if (recurse1 > -1 or recurse2 > -1):
      return max(recurse1, recurse2)
    else:
      return min(recurse1, recurse2)

  val = group_by_two_and_three_helper(num, 0)
  return val


print(group_by_two_and_three(7))
print(group_by_two_and_three(1))
