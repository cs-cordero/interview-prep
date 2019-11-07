from dataclasses import dataclass, field
from typing import Dict, Optional

TERMINAL = "*"


@dataclass
class TrieNode:
    value: str
    children: Dict[str, "TrieNode"] = field(default_factory=dict)


class Trie:
    def __init__(self):
        self.root = TrieNode(TERMINAL)

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            current_node = current_node.children.setdefault(char, TrieNode(char))
        current_node.children.setdefault(TERMINAL, TrieNode(TERMINAL))

    def walk_to_end(self, word: str) -> Optional[TrieNode]:
        current_node = self.root
        for char in word:
            current_node = current_node.children.get(char)
            if not current_node:
                return None
        return current_node

    def search(self, word: str) -> bool:
        last_node = self.walk_to_end(word)
        return last_node and bool(last_node.children.get(TERMINAL))

    def startsWith(self, prefix: str) -> bool:
        return bool(self.walk_to_end(prefix))


obj = Trie()
obj.insert("hello")
print(obj.search("hello"))
print(obj.search("hell"))
print(obj.startsWith("hello"))
print(obj.startsWith("he"))
print(obj.startsWith("hep"))
