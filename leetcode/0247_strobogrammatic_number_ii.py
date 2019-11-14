from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def helper(buildup: List[str], k: int) -> List[str]:
            if k == 0:
                return buildup

            pairs = [("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]
            if k > 3:
                pairs.insert(0, ("0", "0"))

            result = []
            for temp_string in buildup:
                for left, right in pairs:
                    result.append(f"{left}{temp_string}{right}")
            return helper(result, k - 2)

        if n % 2 != 0:
            start = ["0", "1", "8"]
            n -= 1
        else:
            start = [""]
        return helper(start, n)
