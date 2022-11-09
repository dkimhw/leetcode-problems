
"""

Input: array of arrays
  - [[0, 30], [35, 60]]
  - interval_i = [start_i, end_i]
Output: integer
  - min number of rooms required for intervals


Test Cases

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2
  - This is because 0-30 for 1 room
  - [5-10] finishes then you can use the same froom for [15, 20]

Input: intervals = [[7,10],[2,4]]
Output: 1
  - 2, 4 finishes then no conflict with 7,10 - only need one room

Input: [[6,15],[13,20],[6,17]]
Output: 3

Input: [[2,11],[6,16],[11,16]]
Output: 2


Notes
- It seems like if an interval conflicts with any other schedule, that requires an additional room
- It seems like if we sort by start_i - we can check the next interval to see if there is a conflict
- Conflict
  - end of current interval is > next end interval
  - end of current interval is between next start and end interval
- Modifications to the algorithm:
  1. Sorting by start time was correct - you want to worry about the meetings that start first
  2. We need a way to know if there is a free room or not right so that we don't add when there is a conflict

Algorithm:
1. Sort the input array by start_i
2. Create a variable meeting_rooms = 0
3. For each interval in intervals:
  - Check if the curr interval conflicts with next interval
    - increment meeting_rooms
  - else:
    - continue
4. Return meeting_rooms
"""
from typing import List

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    value_list = []
    temp_value = 0
    res = 0

    for interval in intervals:
      value_list.append((interval[0], 1))
      value_list.append((interval[1], -1))

    for value in sorted(value_list):
      # print(value)
      temp_value += value[1]
      # print("tmp_val", temp_value)
      res = max(res, temp_value)
      # print("res: ", res)

    return res

sol = Solution()
print(sol.minMeetingRooms( [[0,30],[5,10],[15,20]])) # 2
print(sol.minMeetingRooms( [[7,10],[2,4]])) # 2
print(sol.minMeetingRooms([[6,15],[13,20],[6,17]])) # 3
print(sol.minMeetingRooms([[13,15],[1,13]])) # 1
print(sol.minMeetingRooms([[2,11],[6,16],[11,16]])) # 2
