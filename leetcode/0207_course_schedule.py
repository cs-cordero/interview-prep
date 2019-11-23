from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prereq_map = defaultdict(list)

        for prereq, course in prerequisites:
            course_to_prereq_map[course].append(prereq)

        visiting = set()
        visited = set()

        def dfs(node: int) -> bool:
            if node in visiting:
                return False

            if node in visited or not course_to_prereq_map[node]:
                return True

            visiting.add(node)
            result = all(dfs(neighbor) for neighbor in course_to_prereq_map[node])
            visiting.remove(node)
            visited.add(node)
            return result

        return all(dfs(node) for node in range(numCourses))
