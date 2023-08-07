
"""
https://leetcode.com/problems/predict-the-winner/


Problem
------------

Input: `nums`
  - list of integers
Output: boolean
  - true if player 1 can win
  - false if player 1 cannot win
Notes
  - if a tie score player 1 wins
  - game rules:
    - each player can choose nums[0] or nums[nums.length - 1] and add it to their score
    - remove that chosen number from `nums`

Example:

Example 1:

Input: nums = [1,5,2]
Output: false
Explanation: Initially, player 1 can choose between 1 and 2.
If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2).
So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return false.
Example 2:

Input: nums = [1,5,233,7]
Output: true
Explanation: Player 1 first chooses 1. Then player 2 has to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.

Walkthrough
--------------

The mechanisms around the game is fairly easy to conceptualize & code.
But the issue is the logic around is there an optimal way to choose that will lead to player 1 winning
  - Greedy right meaning you always take the greater of the two options each time
    - seems to work
    - cannot think of a case where this might fail
  - Fallback - recursion that takes all combinations to see if there is a path for player 1 to win


[1,5,200, 100 ,10,2]

player 1 takes 2
player 2 takes  [1, 5, 200, 100] - 100
player 1 takes [1, 5, 200] - 200

Algorthim (greedy)
1. Create two variables player1 = true; player2 = false; player1_score = 0; player2_score = 0
2. Run a while loop until arr is not empty
  - if player1:
    - set val1 = nums[0]
    - set val2 = nums[len(nums)- 1]
    - if val1 >= val2
      pop off index 0
    - if val2 > val1
      pop off index len(nums) - 1
    - add to player1_score
  - if player2:
    - same logic
3. If player1_score >= player2_score:
  - return true else false



"""
