from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        mapping = {}
        for i, character in enumerate(S):
            start, end = mapping.get(character, (i, i))
            end = i
            mapping[character] = (start, end)

        result = []
        if not mapping:
            return result

        intervals = list(sorted(mapping.values()))

        start, end = intervals[0]
        for other_start, other_end in intervals[1:]:
            if other_start > end:
                result.append(end - start + 1)
                start = other_start
                end = other_end
            else:
                end = max(end, other_end)
        result.append(end - start + 1)
        return result
