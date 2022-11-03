"""

Implementation
* Create a logger class
* shouldPrintMessage
  - Input - integer timestamp, message string
  - Output - boolean
    - True if message should be printed

Test Cases
Logger logger = new Logger();
logger.shouldPrintMessage(1, "foo");  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
logger.shouldPrintMessage(2, "bar");  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
logger.shouldPrintMessage(3, "foo");  // 3 < 11, return false
logger.shouldPrintMessage(8, "bar");  // 8 < 12, return false
logger.shouldPrintMessage(10, "foo"); // 10 < 11, return false
logger.shouldPrintMessage(11, "foo"); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21

Algorithm:
- In Logger class, maintain property message_timestamp which tracks the latest timestamp that a message was printed
- should print message method
  1. Check if `message` exists in `message_timestamp`
  2. If it exists:
    - Check if message is allowed based on input `timestamp` <= `timestamp` (from `message_timestamp`)
      - if true: return true
        - then replace allowed timestamp `message_timestamp[message] = timestamp + self.AT_MOST_SECONDS`
      - else: return false
  3. Else:
    - Add to `message_timestamp[message] = timestamp + self.AT_MOST_SECONDS`
  4. Default: Return true
"""


from collections import defaultdict

class Logger:
  def __init__(self):
    self.message_timestamp = defaultdict(int)
    self.AT_MOST_SECONDS = 10

  def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
    if message in self.message_timestamp:
      allowed_timestamp = self.message_timestamp[message]
      if timestamp < allowed_timestamp:
        return False
      elif timestamp >= allowed_timestamp:
        self.message_timestamp[message] = timestamp + self.AT_MOST_SECONDS
    else:
      self.message_timestamp[message] = timestamp + self.AT_MOST_SECONDS
    return True


logger = Logger()
print(logger.shouldPrintMessage(1, "foo")) #  return true, next allowed timestamp for "foo" is 1 + 10 = 11
print(logger.shouldPrintMessage(2, "bar")); # return true, next allowed timestamp for "bar" is 2 + 10 = 12
print(logger.shouldPrintMessage(3, "foo")); # 3 < 11, return false
print(logger.shouldPrintMessage(8, "bar")); # 8 < 12, return false
print(logger.shouldPrintMessage(10, "foo")); # 10 < 11, return false
print(logger.shouldPrintMessage(11, "foo")); # 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
