from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisite_map = defaultdict(set)
        for prerequisite in prerequisites:
            course_number, requirement = prerequisite
            prerequisite_map[course_number].add(requirement)

        remaining_courses = set(range(numCourses))
        taken_courses = set()
        order = []

        while remaining_courses:
            to_take = []
            for remaining_course in remaining_courses:
                if not prerequisite_map[remaining_course].issubset(taken_courses):
                    continue
                to_take.append(remaining_course)

            if not to_take:
                return []

            for course in to_take:
                remaining_courses.remove(course)
                taken_courses.add(course)
                order.append(course)
        return order
