"""
The read4 API is already defined for you.

    @param buf, a list of characters
    @return an integer
    def read4(buf):

# Below is an example of how the read4 API can be called.
file = File("abcdefghijk") # File is "abcdefghijk", initially file pointer (fp) points to 'a'
buf = [' '] * 4 # Create buffer with enough space to store characters
read4(buf) # read4 returns 4. Now buf = ['a','b','c','d'], fp points to 'e'
read4(buf) # read4 returns 4. Now buf = ['e','f','g','h'], fp points to 'i'
read4(buf) # read4 returns 3. Now buf = ['i','j','k',...], fp points to end of file
"""
from collections import deque
from typing import List


def read4(buffer):
    # This function is provided by Leetcode
    pass


class Solution:
    def __init__(self) -> None:
        self.inner_buffer = deque([])

    def read(self, buf: List[str], n: int) -> int:
        count = 0
        while n > 0:
            while n > 0 and self.inner_buffer:
                buf[count] = self.inner_buffer.popleft()
                n -= 1
                count += 1

            buf4 = [""] * 4
            received = read4(buf4)
            if not received:
                break

            self.inner_buffer.extend([val for val in buf4 if val])
        return count
