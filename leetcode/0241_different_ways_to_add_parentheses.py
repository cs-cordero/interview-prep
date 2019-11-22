import operator
from typing import Any, List


class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        operator_map = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
        }

        def parse_input(s: str) -> List[Any]:
            value = None
            for character in s:
                if character in operator_map:
                    yield value
                    value = None
                    yield operator_map[character]
                else:
                    parsed = int(character)
                    value = parsed if value is None else value * 10 + parsed
            if value is not None:
                yield value

        equation = [value for value in parse_input(input)]

        def helper(lower: int, upper: int) -> List[int]:
            if lower == upper:
                return [equation[lower]]

            result = []
            for pivot in range(lower, upper, 2):
                left = helper(lower, pivot)
                right = helper(pivot + 2, upper)
                op = equation[pivot + 1]
                result.extend(
                    [
                        op(left_val, right_val)
                        for left_val in left
                        for right_val in right
                    ]
                )
            return result

        assert len(equation) % 2 != 0
        return helper(0, len(equation) - 1)
