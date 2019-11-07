class Solution:
    def earliestAcq(self, logs: List[List[int]], N: int) -> int:
        people = list(range(N))

        def find(person: int) -> int:
            if people[person] != person:
                people[person] = find(people[person])
            return people[person]

        for timestamp, person1, person2 in sorted(logs):
            parent1 = find(person1)
            parent2 = find(person2)
            if parent1 == parent2:
                continue

            N -= 1
            if N <= 1:
                return timestamp
            people[parent2] = parent1
        return -1
