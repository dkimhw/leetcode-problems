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

class Solution:
  def aggregate_users(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    users = {}
    for idx, u in enumerate(username):
      if u in users:
        users[u]['timestamp'].append(timestamp[idx])
        users[u]['website'].append(website[idx])
      else:
        users[u] = {}
        users[u]['timestamp'] = []
        users[u]['timestamp'].append(timestamp[idx])
        users[u]['website'] = []
        users[u]['website'].append(website[idx])
    return users

  def get_website_pattern_for_user(self, websites):
    curr_patterns = []
    def all_patterns_recursive_helper(websites, results, curr_result, last_idx):
      if len(curr_result) > 3:
        return
      if len(curr_result) == 3:
        results.append(curr_result[:])
        return

      for idx in range(len(websites)):
        if idx > last_idx:
          curr_result.append(websites[idx])
          all_patterns_recursive_helper(websites, results, curr_result, idx)
          curr_result.pop()

    all_patterns_recursive_helper(websites, curr_patterns, [], -1)
    return curr_patterns

  def count_patterns(self, users):
    patterns = Counter()
    for user, _ in users.items():
      curr_patterns = self.get_website_pattern_for_user(users[user]['website'])
      for curr_pattern in curr_patterns:
        patterns[tuple(curr_pattern)] += 1
    return patterns

  def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    users = self.aggregate_users(username, timestamp, website)
    patterns = self.count_patterns(users)
    most_viewed_pattern = []
    most_views = 0
    for pattern, val in patterns.items():
      if val > most_views:
        most_views = val
        most_viewed_pattern.append(pattern)
    print(patterns)
    return most_viewed_pattern[0]


sol = Solution()
# u1 = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
# t1 = [1,2,3,4,5,6,7,8,9,10]
# w1 = ["home","about","career","home","cart","maps","home","home","about","career"]
# print(sol.mostVisitedPattern(u1, t1, w1))

# u2 = ["ua","ua","ua","ub","ub","ub"]
# t2 = [1,2,3,4,5,6]
# w2 = ["a","b","a","a","b","c"]
# print(sol.mostVisitedPattern(u2, t2, w2))

u3 = ["ua","ua","ua","ub","ub","ub"]
t3 = [1,2,3,4,5,6]
w3 = ["a","b","c","a","b","a"]
print(sol.mostVisitedPattern(u3, t3, w3)) # ["a","b","a"]

# def get_website_pattern_for_user(websites):
#   curr_patterns = []
#   for idx in range(len(websites)):
#     if idx + 2 < len(websites):
#       curr_patterns.append(websites[idx:idx+3])

#   return curr_patterns


# print(get_website_pattern_for_user(['home', 'cart', 'maps', 'home']))

"""
Break conditions
- if the current pattern is === 3, append and return
- recursion
  - loop through each website in order
  - append a new website
  - call function itself with the new appeneded website
  - on return pop added website
"""
# r = []
# def get_all_patterns_recursive_helper(websites, results, curr_result, last_idx):
#   if len(curr_result) > 3:
#     return
#   if len(curr_result) == 3:
#     results.append(curr_result[:])
#     return

#   for idx in range(len(websites)):
#     if idx > last_idx:
#       curr_result.append(websites[idx])
#       get_all_patterns_recursive_helper(websites, results, curr_result, idx)
#       curr_result.pop()

# print(get_all_patterns(['home', 'cart', 'maps', 'home'], r, [], -1))
# print(r)
