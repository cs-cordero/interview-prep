from typing import Iterable, List, Union


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        def perform_calculations(a: int, b: int) -> Iterable[Union[int, float]]:
            yield a + b
            yield a - b
            yield b - a
            yield a * b
            if a:
                yield b / a
            if b:
                yield a / b

        if not nums:
            return False

        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6

        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if i == j:
                    continue
                copy = nums[:]
                copy.remove(num1)
                copy.remove(num2)
                for result in perform_calculations(num1, num2):
                    if self.judgePoint24([result] + copy):
                        return True
        return False


print(Solution().judgePoint24([4, 1, 8, 7]))
print(Solution().judgePoint24([1, 9, 1, 2]))
print(Solution().judgePoint24([1, 2, 1, 2]))
print(Solution().judgePoint24([3, 4, 6, 7]))
print(Solution().judgePoint24([1, 3, 4, 6]))
