from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        reversed_ratings = list(reversed(ratings))
        count = len(ratings)
        fwd = [0 for _ in range(len(ratings))]
        bwd = [0 for _ in range(len(ratings))]

        for i in range(1, len(ratings)):
            fwd[i] = fwd[i - 1] + 1 if ratings[i] > ratings[i - 1] else 0
            bwd[i] = (
                bwd[i - 1] + 1 if reversed_ratings[i] > reversed_ratings[i - 1] else 0
            )

        for a, b in zip(fwd, reversed(bwd)):
            count += max(a, b)

        return count


print(Solution().candy([1, 0, 2]))
print(Solution().candy([1, 2, 2]))
print(Solution().candy([1, 2, 87, 87, 87, 2, 1]))
print(Solution().candy([29, 51, 87, 87, 72, 12]))
print(Solution().candy([1, 3, 2, 2, 1]))
