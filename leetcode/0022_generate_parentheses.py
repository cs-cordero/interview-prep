from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def helper(current: str, opens: int, closes: int) -> None:
            if opens == n and closes == n:
                result.append(current)
                return

            if opens < n:
                helper(f"{current}(", opens + 1, closes)
            if closes < opens:
                helper(f"{current})", opens, closes + 1)

        helper("", 0, 0)
        return result


print(Solution().generateParenthesis(3))
