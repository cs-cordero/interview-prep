from collections import defaultdict
from heapq import heappop, heappush, nlargest
from typing import List


class ReversedOrderString(str):
    def __lt__(self, *args, **kwargs) -> bool:
        return not super().__lt__(*args, **kwargs)


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.query = ""
        self.all_sentences = defaultdict(int)
        self.prefix_map = defaultdict(set)
        for sentence, frequency in zip(sentences, times):
            self.all_sentences[sentence] = frequency
            self.load_prefixes(sentence)

    def input(self, c: str) -> List[str]:
        if c == "#":
            if self.query not in self.all_sentences:
                self.load_prefixes(self.query)
            self.all_sentences[self.query] += 1
            self.query = ""
            return []

        self.query += c
        return self.get_best_sentences()

    def load_prefixes(self, sentence: str) -> None:
        for i in range(1, len(sentence) + 1):
            self.prefix_map[sentence[:i]].add(sentence)

    def get_best_sentences(self) -> List[str]:
        heap = []
        for sentence in self.prefix_map[self.query]:
            frequency = self.all_sentences[sentence]
            heappush(heap, (frequency, ReversedOrderString(sentence)))
            if len(heap) > 3:
                heappop(heap)

        return [str(val) for _, val in nlargest(3, heap)]
