from collections import defaultdict, deque
from typing import List


class Solution:
    def findLadders(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> List[List[str]]:
        edit_map = defaultdict(set)
        all_words = [*wordList, beginWord]
        for word in all_words:
            for i in range(len(word)):
                edit_map[f"{word[:i]}*{word[i+1:]}"].add(word)

        bigraph = defaultdict(set)
        for word in all_words:
            for i in range(len(word)):
                edit_form = f"{word[:i]}*{word[i+1:]}"
                bigraph[word] |= edit_map[edit_form]
            bigraph[word].remove(word)

        shortest_paths = defaultdict(list)
        shortest_paths[beginWord].append([beginWord])
        visited = {beginWord}

        queue = deque([beginWord])
        while queue:
            current = queue.popleft()
            if current == endWord:
                continue
            paths = shortest_paths[current]
            for neighbor in bigraph[current]:
                neighbor_path = shortest_paths[neighbor]

                candidate_path = paths[0] + [neighbor]
                if neighbor_path and len(candidate_path) > len(neighbor_path[0]):
                    continue
                for path in paths:
                    neighbor_path.append(path + [neighbor])
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        return shortest_paths[endWord]
