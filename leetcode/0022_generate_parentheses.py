from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self._recurse("", n, n)

    def _recurse(self, current_str: str, opens: int, closes: int) -> List[str]:
        results: List[str] = []
        if opens > 0:
            results.extend(self._recurse(current_str + "(", opens - 1, closes))
        if closes > opens:
            results.extend(self._recurse(current_str + ")", opens, closes - 1))
        if opens == 0 and closes == 0:
            results.append(current_str)
        return results
