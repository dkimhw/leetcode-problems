"""
https://leetcode.com/problems/analyze-user-website-visit-pattern/

Input:
  - username array
  - timestamp array
  - website visited array
Ouptut:
  - find the website visited pattern that is most used
  - a pattern is a list of three websites -> not necessarily distinct
    - visted four websites: [home, away, love, love]
    - [home, away, love], [away, love, love]

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).


I am thinking one potential method might be to aggregate up theses data by username:
- Joe:
  -[1, 2, 3]
  -[home, about, career]
- James:
  - [4, 5, 6, 7]
  - [home, cart, maps, home]

Algorithm:
0. Reorder the data based on timestamp (not guaranteed to be in order)
1. Create a dictionary called `users`
2. Loop through the three input arrays (choose one)
  - for each username
    - aggregate the website and timestamp data into users
      - if username exists in users
        - append timestamp to `timestamp` property for that user
        - append website to `website` property for that user
3. Create a dictionary called `patterns`
4. Loop through each user in `users`
  - for each user:
    - find three website pattern (home, cart, maps), (cart, maps, home)
      - order matters but you can skip a website
  - increment `patterns` if pattern exists
  - else assign = 1
5. Return patterns that has the most count
"""
from typing import List
from collections import Counter
from collections import defaultdict
from itertools import combinations

class Solution:
  def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    # Create tuples as shown in description
    # The timestamps may not always be pre-ordered (one of the testcases)
    # Sort first based on user, then time (grouping by user)
    # This also helps to maintain order of websites visited in the later part of the solution
    users = defaultdict(list)
    for user, _, site in sorted(zip(username, timestamp, website), key = lambda x: (x[0],x[1])):
      users[user].append(site)     # defaultdicts simplify and optimize code
    patterns = Counter()   # this can also be replaced with a manually created dictionary of counts

		# Get unique 3-sequence (note that website order will automatically be maintained)
		# Note that we take the set of each 3-sequence for each user as they may have repeats
		# For each 3-sequence, count number of users
    for user, sites in users.items():
      seq_combos = combinations(sites, 3)
      seq_combos = set(seq_combos)
      seq_combos = Counter(seq_combos)
      patterns.update(seq_combos)

		# Re-iterating above step for clarity
		# 1. first get all possible 3-sequences combinations(sites, 3)
		# 2. then, count each one once (set)
		# 3. finally, count the number of times we've seen the 3-sequence for every user (patterns.update(Counter))
		# - updating a dictionary will update the value for existing keys accordingly (int in this case)

		# get most frequent 3-sequence sorted lexicographically
    return max(sorted(patterns), key=patterns.get)

sol = Solution()
# u1 = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
# t1 = [1,2,3,4,5,6,7,8,9,10]
# w1 = ["home","about","career","home","cart","maps","home","home","about","career"]
# print(sol.mostVisitedPattern(u1, t1, w1))

# u2 = ["ua","ua","ua","ub","ub","ub"]
# t2 = [1,2,3,4,5,6]
# w2 = ["a","b","a","a","b","c"]
# print(sol.mostVisitedPattern(u2, t2, w2))

# u3 = ["ua","ua","ua","ub","ub","ub"]
# t3 = [1,2,3,4,5,6]
# w3 = ["a","b","c","a","b","a"]
# print(sol.mostVisitedPattern(u3, t3, w3)) # ["a","b","a"]


u4 = ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"]
t4 = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930]
w4 = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
print(sol.mostVisitedPattern(u4, t4, w4))
