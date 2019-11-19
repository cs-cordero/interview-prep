from collections import defaultdict
from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        longest_word_length = max(map(len, words))
        all_letters_seen = set()
        graph = defaultdict(list)
        for i in range(longest_word_length):
            groups = defaultdict(list)
            for word in words:
                all_letters_seen |= set(word)
                if i >= len(word):
                    continue
                key = word[:i]
                groups[key].append(word[i])
            for ordering in groups.values():
                if len(ordering) <= 1:
                    continue
                for j in range(len(ordering) - 1):
                    if ordering[j] == ordering[j + 1]:
                        continue
                    if ordering[j] not in graph[""]:
                        graph[""].append(ordering[j])
                    graph[ordering[j]].append(ordering[j + 1])

        visited = set()
        visiting = set()
        result = []

        def dfs(node: str) -> bool:
            if node in visiting:
                return False
            if node not in graph:
                # This is a leaf node
                visited.add(node)
                result.append(node)
                return True
            visiting.add(node)
            for child in graph[node]:
                if child in visited:
                    continue
                if dfs(child) is False:
                    return False
            visiting.remove(node)
            visited.add(node)
            result.append(node)
            return True

        if graph and dfs("") is False:
            return ""

        result = "".join(reversed(result))
        unused_letters = "".join(sorted(all_letters_seen - set(result)))
        return f"{result}{unused_letters}"
