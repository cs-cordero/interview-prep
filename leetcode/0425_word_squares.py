from collections import defaultdict
from typing import List


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        prefix_map = defaultdict(set)
        for word in words:
            for i in range(1, len(word) + 1):
                prefix_map[word[:i]].add(word)

        answer = []

        def helper(word_square, i):
            if i == len(word_square[0]):
                answer.append(word_square)
                return

            prefix = "".join(word[i] for word in word_square)
            for next_word in prefix_map[prefix]:
                helper(word_square + [next_word], i + 1)

        for word in words:
            helper([word], 1)

        return answer


print(Solution().wordSquares(["wall", "ball", "area", "lead", "lady"]))
print(Solution().wordSquares(["abat", "baba", "atan", "atal"]))
