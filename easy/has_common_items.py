
"""

Input: two arrays
  - What items? - can have different types of data like strings, int
Output: boolean
  - true if there is at least one common item btwn the two arrays
  - do we only care that there is at least one? Do we need to return how many common items?

Examples:

['a', 'b', 'c']
['d', 'e' 'f']
false

['a', 'b', 'c']
['d', 'e' 'a']
true

Check 'a' in the second array, then 'b', then 'c' -  O(n^2)


Questions:
- Is there a space complexity limit? No. Are we allowed to store a set of size `n`

Algorithms - O(n):

- create a set from one of the arrays
- loop through the other unused array
  - check if element exists in set
    - if yes: return true
- return false

"""

def hasCommonItem(lst1, lst2):
  lst1_set = set(lst1)
  for el in lst2:
    if el in lst1_set:
      return True
  return False

print(hasCommonItem(['a', 'b', 'c'], ['d', 'e', 'f'])) # false
print(hasCommonItem(['a', 'b', 'c'], ['d', 'e', 'a'])) # true
