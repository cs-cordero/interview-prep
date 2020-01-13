from collections import defaultdict
from typing import List


class Solution:
    def minimumSemesters(self, N: int, relations: List[List[int]]) -> int:
        graph = defaultdict(list)
        prerequisites = defaultdict(int)
        remaining = set(range(1, N + 1))

        for pre_req, course in relations:
            graph[pre_req].append(course)
            prerequisites[course] += 1

        semester = 0
        workload = [course for course in remaining if prerequisites[course] == 0]

        while workload:
            next_workload = []
            semester += 1
            for course in workload:
                remaining -= {course}
                for next_course in graph[course]:
                    prerequisites[next_course] -= 1
                    if prerequisites[next_course] == 0:
                        next_workload.append(next_course)
            workload = next_workload
        return semester if not remaining else -1
