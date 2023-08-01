
"""

Problem
------------
Input: matrix m x n [ [], [], [] ]
Output: array
  - elements are listed in spiral order from the input matrix

Example
-------------
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Walkthrough
--------------

So it seems like you move in one direction until you cannot
And pattern is:
[right, down, left, up]

Then check if you can keep going in a direction for example right
If you cannot then switch to down if you can

Algorithm
---------------
1. Create variable `result`
2. while matrix is not empty
  2a. Loop over directions array [right, down, left, up]
  2b. Go through the elements in that direction & append to result (needs to be expanded) until you cannot go in that direction
    - expand on what elements are in that direction
    - replace element we visited as 'visited'
  2c. continue to the next direction
3. Return result

2b Expand
---------------
Notes:
  - I think we need some way to know where we currently are in the matrix
    - Then based on that & the direction we are currently on we can identify the elements that need to be visited
    - For example, if we are [0, 3] then we can use the 3 to go down or retrieve all column values in 3
  - Either pop or keep track of which locations you already visited or mark it as 'visited'

  1. Current location logic
    - declare current_loc = [0, 0]
    - as you move forward left/right/up/down - increase corresponding index
  2. Need logic to identify whether we've reached the end of that direction
    - If we were moving left, if current_loc[0] + 1 == len(matrix[0]) then return false (cannot move further)
    - If we were moving right, if current_loc[0] - 1 < 0 then return false (cannot move further)
    - If we were moving up, if current_loc[1] - 1 < 0 then return false (cannot move further)
    - If we were
  3. Need logic by using current location & direction to return a list of elements that we need to visit


"""
