from typing import List


class Solution:
    def findReplaceString(
        self, S: str, indexes: List[int], sources: List[str], targets: List[str]
    ) -> str:
        sorted_indexes = sorted(range(len(indexes)), key=lambda x: indexes[x])

        answer = ""
        expected_index = 0
        for i in sorted_indexes:
            index, source, target = indexes[i], sources[i], targets[i]
            answer += S[expected_index:index]
            original = S[index : index + len(source)]
            answer += target if original == source else original
            expected_index = index + len(source)
        if expected_index < len(S):
            answer += S[expected_index:]
        return answer
