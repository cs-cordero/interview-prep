from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        generic_to_words = defaultdict(set)
        word_to_generics = defaultdict(set)
        word_list = set(wordList)
        visited = defaultdict(lambda: float("inf"))

        for word in [beginWord, endWord, *wordList]:
            for i, _ in enumerate(word):
                generic_form = f"{word[:i]}*{word[i+1:]}"
                generic_to_words[generic_form].add(word)
                word_to_generics[word].add(generic_form)

        queue = deque([(beginWord, 0)])
        while queue:
            word, operations = queue.popleft()
            visited[word] = min(visited[word], operations + 1)

            children = {
                (shares_generic_form, operations + 1)
                for generic_representation in word_to_generics[word]
                for shares_generic_form in generic_to_words[generic_representation]
                if shares_generic_form != word
                and shares_generic_form not in visited
                and shares_generic_form in word_list
            }
            queue.extend(children)
        return visited[endWord] if endWord in visited else 0
