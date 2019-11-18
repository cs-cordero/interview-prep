from collections import defaultdict
from typing import List


class StreamChecker:
    def __init__(self, words: List[str]):
        def recursive_defaultdict_factory():
            return defaultdict(recursive_defaultdict_factory)

        self.waitlist = []
        self.trie = recursive_defaultdict_factory()
        for word in words:
            sub_trie = self.trie
            for letter in word:
                sub_trie = sub_trie[letter]
            sub_trie["#"] = True

    def query(self, letter: str) -> bool:
        next_waitlist = []
        found_word = False
        for sub_trie in self.waitlist + [self.trie]:
            if letter not in sub_trie:
                continue
            if "#" in sub_trie[letter]:
                found_word = True
            next_waitlist.append(sub_trie[letter])
        self.waitlist = next_waitlist
        return found_word
