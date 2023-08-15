
"""

https://leetcode.com/problems/minimum-time-to-complete-trips/

Problem:
------------
Input: array `time`, totalTrips integer
  - time[i] denotes the time taken by the ith bus to complete one trip.
  - denotes the number of trips all buses should make in total.
Output: integer
  - return the minimum time required for all buses to complete at least totalTrips
Notes:
  - Each bus can make multiple trips successively; that is, the next trip can start immediately after completing the current trip.


Example:
-------------
Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0].
  The total number of trips completed is 1 + 0 + 0 = 1.
- At time t = 2, the number of trips completed by each bus are [2,1,0].
  The total number of trips completed is 2 + 1 + 0 = 3.
- At time t = 3, the number of trips completed by each bus are [3,1,1].
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.

Input: time = [2], totalTrips = 1
Output: 2
Explanation:
There is only one bus, and it will complete its first trip at t = 2.
So the minimum time needed to complete 1 trip is 2.

Walkthrough
---------------
current_t = 1
while curr_total < total_trips

At t = 1 --> check how many times can you go

[1,2,3]

t % times[i] == 0 then completed[i] =  t / times[i]

curr_total += how many trips were completed so far


Optimization
----------------

- maybe we can find the largest number and use that as the base
- so max(time)

[1, 2, 3, 90000]

90000 so we need at least t = 90000
tripLength = 95000


[9,3,10,5], 2

So above optimization does not work for this scenario
current_time = max(time) if max(time) < tripLength else min(time)


New Approach
----------------
From 1 to worst case time. The worst case here is: highest time[i] * time duration
  - i.e. [90000], 2 = 180000

Search between 1 to worst case for the minimum time to satisfy the trip
  - time = [1,2,3], totalTrips = 5; 3
  - Search between 1 to 15
    - midpoint: 7
    - if midpoint can be re-created using [1, 2, 3]
      - then we want to look at the left side of the array
    - else we want to look at the right side of the array
  - Helper function to check if midpoint can be recreated
    - declare variable result
    - loop through `time`
      - add to result math.floor(time[i] / midpoint)
    - return result == midpoint
"""
from typing import List

class Solution:
  def minimumTime(self, time: List[int], totalTrips: int) -> int:
    current_time = max(time) if max(time) < totalTrips else min(time)
    # print(current_time)
    curr_trip_total = 0
    completed = [0] * len(time)
    while True:
      # need to optimize this
      curr_trip_total = 0
      for idx in range(len(completed)):
        completed[idx] = int(current_time / time[idx]) # if current_time % time[idx] == 0 else completed[idx]
        curr_trip_total += completed[idx]
      # print(completed)
      if curr_trip_total >= totalTrips:
        break
      current_time += 1

    return current_time


sol = Solution()
# print(sol.minimumTime([1,2,3], 5))
print(sol.minimumTime([9,3,10,5], 2)) # 5
