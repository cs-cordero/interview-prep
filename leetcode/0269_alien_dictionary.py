from collections import defaultdict, deque
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        letter_map = {}
        last_char = []
        for word in words:
            current = letter_map
            for i, letter in enumerate(word):
                if len(last_char) == i:
                    last_char.append(letter)
                if letter != last_char[i]:
                    if letter in current:
                        return ""
                    else:
                        last_char[i] = letter
                current = current.setdefault(letter, {})

        digraph = defaultdict(list)
        queue = deque([letter_map])
        while queue:
            current = queue.popleft()
            if not current:
                continue

            parent, *children = current.keys()
            digraph[parent]
            for child in children:
                digraph[parent].append(child)
                digraph[child]
                parent = child

            for sub_dict in current.values():
                queue.append(sub_dict)

        visited = set()
        visiting = set()
        top_sorted = []

        def helper(letter: str) -> bool:
            if letter in visiting:
                return False
            elif letter in visited:
                return True

            visiting.add(letter)
            for neighbor in digraph[letter]:
                if not helper(neighbor):
                    return False
            visiting.remove(letter)

            visited.add(letter)
            top_sorted.append(letter)
            return True

        for letter in digraph:
            if helper(letter) is False:
                return ""
        return "".join(reversed(top_sorted))


print(Solution().alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
print(Solution().alienOrder(["z", "x"]))
print(Solution().alienOrder(["z", "x", "z"]))
print(Solution().alienOrder(["aa", "abb", "aba"]))
