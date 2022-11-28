

from collections import Counter
from collections import defaultdict
from itertools import combinations




u1 = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
t1 = [1,2,3,4,5,6,7,8,9,10]
w1 = ["home","about","career","home","cart","maps","home","home","about","career"]

users = defaultdict(list)
for user, _, site in sorted(zip(u1, t1, w1), key = lambda x: (x[0],x[1])):
  users[user].append(site)     # defaultdicts simplify and optimize code
patterns = Counter()   # this can also be replaced with a manually created dictionary of counts

for user, sites in users.items():
  seq_combos = combinations(sites, 3)
  seq_combos = set(seq_combos)
  seq_combos = Counter(seq_combos)
  patterns.update(seq_combos)

print(users)
print(patterns)


def three_combinations(websites):
  combinations = Counter()
  def three_combinations_recursive(websites, curr_combination, curr_idx, results):
    if len(curr_combination) == 3:
      t = tuple(curr_combination[:])
      combinations[t] += 1
      return

    for idx in range(len(websites)):
      if idx > curr_idx:
        curr_combination.append(websites[curr_idx])
        three_combinations_recursive(websites, curr_combination, idx, results)
        curr_combination.pop()

  three_combinations_recursive(websites, [], -1, combinations)
  return combinations

# web1 = ['home', 'cart', 'maps', 'home']
# print(three_combinations(web1))

patterns2 = Counter()   # this can also be replaced with a manually created dictionary of counts

for user, sites in users.items():
  seq_combos = three_combinations(sites)
  seq_combos = set(seq_combos)
  seq_combos = Counter(seq_combos)
  patterns2.update(seq_combos)

print("Patterns2: ", patterns)
