

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
- Create results array and counter integer variables
- Loop through the interval (while loop) and for each interval pair:
  - Check that end_i is btwn start_i+1 and end_i+1 and Check that end_i is > end_i+1
  - Append min of (start_i, start_i+1) , max (end_i, end_i+1)
  - increment counter by += 2
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
    while curr_idx_counter < len(intervals):
      if curr_idx_counter == 0:
        results.append(intervals[curr_idx_counter])
        curr_idx_counter += 1

      if curr_idx_counter > 0 and curr_idx_counter <= len(intervals) - 1:
        curr_start = intervals[curr_idx_counter][0]
        curr_end = intervals[curr_idx_counter][1]
        result_start = results[len(results) - 1][0]
        result_end = results[len(results) - 1][1]

        if (result_end >= curr_start and result_end <= curr_end) or (result_end > curr_end):
          min_start_interval = min(curr_start, result_start)
          max_end_interval = max(curr_end, result_end)
          results[len(results) - 1] = [min_start_interval, max_end_interval]
          curr_idx_counter += 1
        else:
          results.append(intervals[curr_idx_counter])
          curr_idx_counter += 1
    return results

sol = Solution()
# print(sol.merge([[1,3],[2,6],[8,10],[15,18]])) # Output: [[1,6],[8,10],[15,18]]
# print(sol.merge([[1,4],[4,5]])) # Output:  [[1,5]]
# print(sol.merge( [[1,4],[0,4]])) # Output:  [[0,4]]
# print(sol.merge([[1,4],[2,3]])) # Output: [[1,4]]
# print(sol.merge([[1,4],[0,2],[3,5]])) # [[0,5]]
print(sol.merge([[1,3]])) # [[1,3]]

# x = [[1,4],[0,4]]
# def sortByIntervalStart(interval):
#   return interval[0]
# x.sort(key = sortByIntervalStart)
# print(x)
