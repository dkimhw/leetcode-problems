

"""

Input: array of intervals (array of arrays)
Output: array of non-overlapping intervals (array of arrays)
  - covers all the intervals in the input

Test Cases:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
  - You overlap if either the start or end of either intervals are between
  - start and end

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Algorithm O(n log n):
- Sort the intervals based on start
- Loop through the interval and for each interval pair:
  - Check that end_i is btwn start_i+1 and end_i+1
- If btwn:
  - merge the two intervals and add to results array
  - skip the i+1 interval
- else:
  - continue onto the next interval
"""

from typing import List

class Solution:
  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    def sortByIntervalStart(interval):
      return interval[0]
    intervals.sort(key = sortByIntervalStart)
    results = []
    curr_idx_counter = 0
    for idx in range(len(intervals)):
      if curr_idx_counter <= idx:
        if idx + 1 <= len(intervals) - 1 and intervals[idx][1] >= intervals[idx + 1][0] and intervals[idx][1] <= intervals[idx + 1][1]:
          min_start_interval = min(intervals[idx][0], intervals[idx + 1][0])
          max_end_interval = max(intervals[idx][0], intervals[idx + 1][1])
          results.append([min_start_interval, max_end_interval])
          curr_idx_counter += 2
        elif idx + 1 <= len(intervals) - 1 and intervals[idx][1] > intervals[idx + 1][1]:
          min_start_interval = min(intervals[idx][0], intervals[idx + 1][0])
          max_end_interval = max(intervals[idx][0], intervals[idx + 1][1])
          results.append([min_start_interval, max_end_interval])
          curr_idx_counter += 2
        else:
          results.append(intervals[idx])
          curr_idx_counter += 1
    return results

sol = Solution()
print(sol.merge([[1,3],[2,6],[8,10],[15,18]])) # Output: [[1,6],[8,10],[15,18]]
print(sol.merge([[1,4],[4,5]])) # Output:  [[1,5]]
print(sol.merge( [[1,4],[0,4]])) # Output:  [[0,4]]
print(sol.merge([[1,4],[2,3]])) # Output: [[1,4]]
print(sol.merge([[1,4],[0,2],[3,5]])) # [[0,5]]

# x = [[1,4],[0,4]]
# def sortByIntervalStart(interval):
#   return interval[0]
# x.sort(key = sortByIntervalStart)
# print(x)
