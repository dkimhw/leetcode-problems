"""
https://leetcode.com/problems/design-an-ordered-stream/

Input: n pairs (idkey, value)
  - idkey - unique intger btwn 1 and n
  - Comes in arbitrary order
Output:
  - Return a chunk after each insertion
    - Chunk is starting from the ptr to until there is no None
  - The list must be ordered in increasing order

Example:
Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Explanation
// Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
OrderedStream os = new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
// Concatentating all the chunks returned:
// [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
// The resulting order is the same as the order above.

Algorithm - insert:
- Create a `ptr` in constructor to track the current position of the stream
- Create an array of size [] * n in constructor
- Insert the (idKey, value) pair at the the current ptr using slice method
- Check if current ptr idx is not null then start to loop until there is none
  - return the chunk
"""

from typing import List

class OrderedStream:
  def __init__(self, n: int):
    self.n = [None] * n
    self.ptr = 0

  def insert(self, idKey: int, value: str) -> List[str]:
    self.n[idKey - 1] = value

    if self.n[self.ptr] is not None:
      chunk = []
      while self.ptr < len(self.n) and self.n[self.ptr] is not None:
        chunk.append(self.n[self.ptr])
        self.ptr += 1

      return chunk
    else:
      return []



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)

os = OrderedStream(5);
a = os.insert(3, "ccccc"); # Inserts (3, "ccccc"), returns [].
b = os.insert(1, "aaaaa"); # Inserts (1, "aaaaa"), returns ["aaaaa"].
c = os.insert(2, "bbbbb"); # Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
d = os.insert(5, "eeeee"); # Inserts (5, "eeeee"), returns [].
e = os.insert(4, "ddddd"); # Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].

print(a)
print(b)
print(c)
print(d)
print(e)
print(os.n)
