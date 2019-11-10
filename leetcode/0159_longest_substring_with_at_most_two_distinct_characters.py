from collections import defaultdict


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        distinct = set()
        counts = defaultdict(int)

        longest = 0

        begin = 0
        for end, character in enumerate(s):
            counts[character] += 1
            distinct.add(character)

            while len(distinct) > 2:
                counts[s[begin]] -= 1
                if counts[s[begin]] == 0:
                    distinct.remove(s[begin])
                begin += 1

            longest = max(longest, end - begin + 1)
        return longest
