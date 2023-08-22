
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


Optimization Ideas
----------------

- maybe we can find the largest number and use that as the base
- so max(time)

[1, 2, 3, 90000]

90000 so we need at least t = 90000
tripLength = 95000


[9,3,10,5], 2

So above optimization does not work for this scenario.

I think the search area has to be from 1 to the worst case which is taking the worst time possible for
a bus trip * the total trips.


New Approach
----------------
From 1 to worst case time. The worst case here is: highest time[i] * time duration
  - i.e. [90000], 2 = 180000

Search between 1 to worst case for the minimum time to satisfy the trip
  - Binary search
  - time = [1,2,3], totalTrips = 5; 3
  - Search between 1 to 15
    - midpoint: 7
    - Found how many trips were made using t = 7
      - if this number was > totalTrips - we want to look at the left side of the array
      - else we want to look at the right side of the array
    - here midpoint is when trips == totalTrips
  - Helper function to check if midpoint can be recreated
    - declare variable result
    - loop through `time`
      - add to result math.floor(time[i] / midpoint)
"""
from typing import List

class Solution:
  def isTripPossible(self, time: List[int], totalTrips: int, minTime: int) -> bool:
    result = 0
    for t in time:
      result += (minTime // t)
    return result

  def minimumTime(self, time: List[int], totalTrips: int) -> int:
    left = 0
    right = max(time) * totalTrips
    curr_min_time = 0
    cnt = 0

    #while left < right:
    while cnt < 7:
      midpoint = (left + right) // 2
      # if midpoint that I chose was a time that is possible given time & totalTrips, I want to go left
      trips = self.isTripPossible(time, totalTrips, midpoint) # need function here
      if trips == totalTrips:
        return midpoint
      elif trips >= totalTrips:
        right = midpoint
        curr_min_time = midpoint
      else:
        left = midpoint
      print("is possible", trips)
      print("midpoint", midpoint)
      print(left, right)
      cnt += 1
    print("curr_min_time", curr_min_time)





sol = Solution()
# print(sol.isTripPossible([1,2,3], 5, 3))
# print(sol.isTripPossible([1,2,3], 5, 0))
print(sol.minimumTime([1,2,3], 5))
# print(sol.minimumTime([9,3,10,5], 2)) # 5
