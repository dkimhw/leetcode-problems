"""
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

Input: list of song duration List[int]
Output: integer
  - count of pairs of songs where total duration is divisible by 60 (in seconds)

Test Case

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible by 60.


The brute force way would be O(n^2). Is there a solution where the complexity is lower?

What if we had a dictionary of durations:
- Counter: {30: 1, 20: 1, 150: 1, 100: 1, 40: 1}
- 340 O(n)
- {30: [30, 90, 150, 210, ...]} O(n)

Algorithm Attemp 1 (no good):
1. Create a counter of all the elements in `time` O(n)
2. Calculate maximum value 2 * max value will be the threshold O(n)
3. Create a new dictionary where key is the value and value is an array of possible values O(1)
4. For each key - generate all possible values up to 2 * max value (m/60 * n)


Hint:
We only need to consider each song length modulo 60.
We can count the number of songs with (length % 60) equal to r, and store that in an array of size 60.

Because I think these are remainders right

Algorithm Attempt 2:
1. Create an array song_duration_remainder of size 60
2. Loop through time
  - modulus each duration % 60
  - use the returned value as the index of the array song_duration_remainder and increment by 1
3. Loop through song_duration_remainder
  - Have a left and right index
  - left start from index 1 and right last index and works towards the middle incrementing left each time and decrementing right each time
  - Logic for counting the pairs
    - index 1: 2
    - index 59: 3
    - No this is combination formula: n! / (2! (n - 2)!)
4. For index 0
  - 2 pairs = 1
    - if it's
"""
from typing import List

class Solution:
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    pass
