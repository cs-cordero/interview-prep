from collections import defaultdict
from heapq import heapify, heappop
from typing import List


class Master:
    # Provided by Leetcode
    ...


class Solution:
    def findSecretWord(self, wordlist: List[str], master: "Master") -> None:
        candidates = set()
        match_map = defaultdict(lambda: defaultdict(set))
        ranks = defaultdict(int)
        for i, word in enumerate(wordlist):
            candidates.add(word)
            for j in range(i + 1, len(wordlist)):
                other_word = wordlist[j]
                matches = sum(a == b for a, b in zip(word, other_word))
                match_map[word][matches].add(other_word)
                match_map[other_word][matches].add(word)
                ranks[word] += 1
                ranks[other_word] += 1

        heap = [(rank, word) for word, rank in ranks.items()]
        heapify(heap)

        while len(candidates) > 0:
            while heap and heap[0][1] not in candidates:
                heappop(heap)
            if not heap:
                continue
            _, guess = heappop(heap)
            result = master.guess(guess)
            if result == 6:
                break
            candidates.remove(guess)
            candidates &= match_map[guess][result]
