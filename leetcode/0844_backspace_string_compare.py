from typing import List


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def parse_string(characters: str) -> List[str]:
            s = []
            for character in characters:
                if character != "#":
                    s.append(character)
                elif s:
                    s.pop()
            return s

        return parse_string(S) == parse_string(T)


Solution().backspaceCompare("y#fo##f", "y#f#o##f")
