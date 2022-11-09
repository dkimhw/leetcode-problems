
"""

https://leetcode.com/problems/meeting-rooms-ii/solutions/168762/meeting-rooms-ii/

Algorithm

1. Sort the given meetings by their start time.
2. Initialize a new min-heap and add the first meeting's ending time to the heap. We simply need to keep track of the ending times as that tells us when a meeting room will get free.
3. For every meeting room check if the minimum element of the heap i.e. the room at the top of the heap is free or not.
4. If the room is free, then we extract the topmost element and add it back with the ending time of the current meeting we are processing.
5. If not, then we allocate a new room and add it to the heap.
After processing all the meetings, the size of the heap will tell us the number of rooms allocated. This will be the minimum number of rooms needed to accommodate all the meetings.

"""
from typing import List
import heapq

class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    if not intervals:
      return 0

    # heap initialization
    free_rooms = []
    heapq.heapify(free_rooms)

    # sort by start date
    intervals.sort(key = lambda interval: interval[0])

    # add first interval
    heapq.heappush(free_rooms, intervals[0][1])

    for idx in range(1, len(intervals)):
      # if a meeting start is greater than or equal to the top most value in heap
      # i.e. the earliest time a meeting will end then there is a free room
      if free_rooms[0] <= intervals[idx][0]:
        print("hello")
        heapq.heappop(free_rooms)
      # If a new room is to be assigned, then also we add to the heap,
      # If an old room is allocated, then also we have to add to the heap with updated end time.
      heapq.heappush(free_rooms, intervals[idx][1])
    return len(free_rooms)


sol = Solution()
print(sol.minMeetingRooms( [[0,30],[5,10],[15,20]])) # 2
print(sol.minMeetingRooms( [[7,10],[2,4]])) # 1
print(sol.minMeetingRooms([[6,15],[13,20],[6,17]])) # 3
print(sol.minMeetingRooms([[13,15],[1,13]])) # 1
print(sol.minMeetingRooms([[2,11],[6,16],[11,16]])) # 2
