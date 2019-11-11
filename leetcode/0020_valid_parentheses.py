class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "[",
        }
        open_brackets = {"(", "[", "{"}
        for character in s:
            if character in open_brackets:
                stack.append(character)
                continue

            expected = bracket_map[character]
            if not stack or stack[-1] != expected:
                return False
            stack.pop()
        return not bool(stack)
