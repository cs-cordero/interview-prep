from copy import copy


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        if not source:
            return -1

        dp = [{} for _ in range(len(source))]
        dp[len(source) - 1][source[-1]] = len(source) - 1

        if len(source) > 1:
            for i in range(len(source) - 2, -1, -1):
                dp[i] = copy(dp[i + 1])
                dp[i][source[i]] = i

        answer = 0
        dp_i = 0
        for target_i, target_char in enumerate(target):
            if dp[0].get(target_char) is None:
                return -1

            location = dp[dp_i].get(target_char)
            if location is None:
                answer += 1
                dp_i = dp[0][target_char] + 1
            elif location + 1 >= len(dp):
                answer += 1
                dp_i = 0
            else:
                dp_i = location + 1
        if dp_i > 0:
            answer += 1
        return answer


# print(Solution().shortestWay("abc", "abcbc"))
print(Solution().shortestWay("adbsc", "addddddddddddsbc"))
