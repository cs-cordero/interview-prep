from collections import deque


class Solution:
    def new21Game(self, N: int, K: int, W: int) -> float:
        if not K or not N or not W:
            return 1.0

        successes = [0 for _ in range(K)]
        successes[-1] = (N - (K - 1)) / W

        additional = (1.0 / W) * successes[-1]
        window = deque([additional])
        for i in range(K - 2, -1, -1):
            probability = max(min(N, i + W) - K + 1, 0) / float(W)
            probability += additional
            successes[i] = probability

            next_additional = (1.0 / W) * probability
            additional += next_additional
            window.appendleft(next_additional)
            while len(window) > W:
                additional -= window.pop()

        return successes[0]


print(Solution().new21Game(10, 1, 10))
print(Solution().new21Game(6, 1, 10))
print(Solution().new21Game(21, 17, 10))
print(Solution().new21Game(5710, 5070, 8516))
