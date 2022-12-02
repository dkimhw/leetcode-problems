"""

Implementation
* Implement init
  - capacity (int)
* get method
  - Input: Key (int)
  - Output: Returns the value of the `key` if the key exists else -1
* put method
  - Input: Key (int), Val (int)
  - Output: returns None
  - Side Effect
    - Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache.
    - If the number of keys exceeds the capacity from this operation, evict the least recently used key.

Test Cases

lru = LRUCache(2)
lru.put(1, 1) # cache is {1=1}
lru.put(2, 2) # cache is {1=1, 2=2}
print(lru.get(1))    # return 1
lru.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lru.get(2)) # returns -1 (not found)
lru.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lru.get(1)) # return -1 (not found)
print(lru.get(3)) # return 3
print(lru.get(4)) # return 4

I use 1. Goes into stack [1]
I use 2. Goes into stack from front [2, 1]
I use 3 for the first time. Goes into stack from front [3, 2] and evict 1

Algorithm:
- In init - maintain property `cache` (ordered dict)
- get method
  - return `cache[key]` if key exists else -1
  - Since I used the "k-v" - move the k-v to the end of the dictionary indicating that it has been used most recently
- put method
  - If key exists: update value
  - If key does not exists and under capacity: add value to cache
- put eviction logic**
  - If full:
    - evict the least recently used key-value pair
    - add the new k-v pair
"""
from collections import OrderedDict
class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = OrderedDict()

  def get(self, key: int) -> int:
    if key in self.cache:
      self.cache.move_to_end(key)
      return self.cache[key]
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self.cache[key] = value
      self.cache.move_to_end(key)
    elif key not in self.cache and len(self.cache.keys()) < self.capacity:
      self.cache[key] = value
      self.cache.move_to_end(key)
    else:
      self.cache.popitem(last = False)
      self.cache[key] = value
      self.cache.move_to_end(key)



lru = LRUCache(2)
lru.put(1, 1) # cache is {1=1}
lru.put(2, 2) # cache is {1=1, 2=2}
print(lru.get(1))    # return 1
lru.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
print(lru.get(2)) # returns -1 (not found)
lru.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lru.get(1)) # return -1 (not found)
print(lru.get(3)) # return 3
print(lru.get(4)) # return 4
