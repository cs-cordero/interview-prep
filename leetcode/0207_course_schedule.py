from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for requirement, course in prerequisites:
            graph[requirement].append(course)

        visited = set()
        visiting = set()

        def helper(course: int) -> bool:
            if course in visiting:
                return False
            elif course in visited:
                return True

            visiting.add(course)
            for next_course in graph[course]:
                if not helper(next_course):
                    return False
            visited.update(visiting)
            visiting.remove(course)
            return True

        return all(helper(course) for course in range(numCourses))
