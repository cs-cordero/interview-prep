from collections import deque
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        tree = {}
        all_variables = set()

        for i, (a, b) in enumerate(equations):
            tree.setdefault(a, {})[b] = values[i]
            tree.setdefault(b, {})[a] = 1 / values[i]
            all_variables.add(a)
            all_variables.add(b)

        def bfs(var: str, target: str) -> float:
            if var == target and var in all_variables:
                return 1.0

            queue = deque([(var, 1)])
            visited = {var}
            while queue:
                current, running_value = queue.popleft()
                if current not in all_variables:
                    return -1.0

                for child, child_value in tree[current].items():
                    if child in visited:
                        continue
                    visited.add(child)
                    amount_to_child = running_value * child_value
                    tree[var].setdefault(child, amount_to_child)
                    if child == target:
                        return amount_to_child
                    queue.append((child, amount_to_child))
            return -1.0

        answers = []
        for source, target in queries:
            answers.append(bfs(source, target))
        return answers


equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

print(Solution().calcEquation(equations, values, queries))
