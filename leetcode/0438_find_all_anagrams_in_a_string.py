from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(p) > len(s):
            return []

        counter = [0] * 26
        for char in p:
            counter[ord(char) - 97] += 1

        window_counter = [0] * 26
        for i in range(len(p)):
            window_counter[ord(s[i]) - 97] += 1

        result = []
        begin = 0
        end = len(p)
        while end <= len(s):
            if window_counter == counter:
                result.append(begin)
            if end == len(s):
                break
            window_counter[ord(s[end]) - 97] += 1
            window_counter[ord(s[begin]) - 97] -= 1
            end += 1
            begin += 1
        return result
