"""
https://leetcode.com/problems/number-of-islands/

Input: m x n grid
Output: integer
  - number of islands
  - definition: surround by water. Joined consecutively by land
  - assume: all outer edges of the grid are water


Test Cases:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

One potential approach: BFS
  - I guess one thing to note here is that once searched - we don't want to restart the BFS for those search nodes right?
    - We need a global unsearched grid - remove from this as BFS runs
  - Then we keep looping until unsearched grid space is empty


Overall Algorithm:
  1. Create a variable `final_result`
  2. Create a variable called `not_visited` list and populate it with tuples of element indexes i.e. (0, 0)
  2. While :
    - If "1", run BFS
      - Increment `final_result` by 1
    - If "0", continue to next element
  3. Return `final_result`

BFS Algorithm:
  1. Create a set `to_search` and append starting node
  2. Create a set `searched`
  3. While `to_search` is not empty:
    - pop from `to_search`
    - get neighbors using the popped value
      - Given a tuple of indexes:
      - Check (row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)
        - If out of range - don't include it
    - if a neighbor is not in `searched` and == 1 and not in `not_visited`, append to `to_search`
  4. Take searched and remove from `not_visited` list, the visited indexes
"""
from typing import List

class Solution:
  def get_neighbor(self, node: tuple, grid: List[List[str]]):
    valid_nodes = []
    m = len(grid)
    n = len(grid[0])
    if node[0] + 1 <= m:
      valid_nodes.append(tuple([node[0] + 1, node[1]]))

    if node[0] - 1 >= 0:
      valid_nodes.append(tuple([node[0] - 1, node[1]]))

    if node[1] + 1 <= n:
      valid_nodes.append(tuple([node[0], node[1] + 1]))

    if node[1] - 1 >= 0:
      valid_nodes.append(tuple([node[0], node[1] - 1]))
    return valid_nodes

  def bfs_islands(self, grid: List[List[str]], starting_node: tuple, not_visited: List[tuple]):
    to_search = set()
    searched = set()
    to_search.add(starting_node)

    while len(to_search) > 0:
      curr_node = to_search.pop()
      searched.add(curr_node)
      neighbors = self.get_neighbor(curr_node, grid)
      for neighbor in neighbors:
        if neighbor not in searched and grid[curr_node[0]][curr_node[1]] == '1' and neighbor in not_visited:
          to_search.add(neighbor)
    print(searched)
    # Remove from not_visited

  def numIslands(self, grid: List[List[str]]) -> int:
    final_result = 0
    not_visited = []
    for idx in range(len(grid)):
      for jdx in range(len(grid[idx])):
        not_visited.append(tuple([idx, jdx]))
    print(not_visited)


sol = Solution()

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
v = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (3, 0), (3, 1), (3, 2), (3, 3), (3, 4)]
print(sol.bfs_islands(grid, (0, 0), v))

# print(sol.numIslands(grid))


# grid2 = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# print(sol.numIslands(grid2))
