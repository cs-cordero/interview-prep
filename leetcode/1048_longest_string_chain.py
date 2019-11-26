import string
from collections import Counter, defaultdict, deque
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        group_by_length = defaultdict(list)
        shortest_length = float("inf")
        longest_length = float("-inf")
        for word in words:
            group_by_length[len(word)].append((word, Counter(word)))
            shortest_length = min(shortest_length, len(word))
            longest_length = max(longest_length, len(word))

        def can_chain(counterA: Counter, counterB: Counter) -> bool:
            # A should be a smaller count than B
            differences = 0
            for letter in string.ascii_lowercase:
                countA = counterA[letter]
                countB = counterB[letter]
                differences += countB - countA
                if countB - countA < 0 or differences > 1:
                    return False
            return True

        graph = defaultdict(list)
        for length, words in group_by_length.items():
            for word, counter in words:
                candidates = group_by_length.get(length + 1, [])
                for (candidate, candidate_counter) in candidates:
                    if can_chain(counter, candidate_counter):
                        graph[word].append(candidate)

        longest = 1
        for i in range(shortest_length, 17):
            if (longest_length - (i - 1)) <= longest:
                break
            queue = deque([(word, 1) for word, _ in group_by_length[i]])
            visited = set()
            while queue:
                word, length = queue.popleft()
                longest = max(longest, length)
                for next_word in graph[word]:
                    if next_word in visited:
                        continue
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
        return longest
