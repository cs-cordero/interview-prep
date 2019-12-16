from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        answer = set()
        removals = float("inf")

        def has_valid_parentheses(candidate: str) -> bool:
            open_parens = 0
            for value in candidate:
                if value == "(":
                    open_parens += 1
                elif value == ")":
                    if open_parens <= 0:
                        return False
                    else:
                        open_parens -= 1
            return open_parens == 0

        def dfs(
            index: int,
            current: str,
            removes: int = 0,
            openings: int = 0,
            closings: int = 0,
        ) -> None:
            nonlocal removals

            if removes > removals or closings > openings:
                return None

            if index == len(s):
                if has_valid_parentheses(current):
                    if removes < removals:
                        answer.clear()
                        removals = removes
                    answer.add(current)
                return None

            if s[index] not in ("(", ")"):
                dfs(
                    index + 1, f"{current}{s[index]}", removes, openings, closings,
                )
            else:
                dfs(
                    index + 1,
                    f"{current}{s[index]}",
                    removes,
                    openings + (s[index] == "("),
                    closings + (s[index] == ")"),
                )
                dfs(
                    index + 1, current, removes + 1, openings, closings,
                )

        dfs(0, "")
        return list(answer)


print(Solution().removeInvalidParentheses("()())()"))
print(Solution().removeInvalidParentheses("d)"))
print(Solution().removeInvalidParentheses(")((())))))()(((l(((("))
