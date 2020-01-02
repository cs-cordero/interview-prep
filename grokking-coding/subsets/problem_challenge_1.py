import operator
import string
from typing import List, Union

OPERATION_MAP = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
}


def diff_ways_to_evaluate_expression(s: str) -> List[int]:
    def helper(sub_expression: List[Union[int, str]]) -> List[int]:
        if len(sub_expression) == 1:
            return [sub_expression[0]]

        result = []
        for i in range(1, len(sub_expression), 2):
            left = helper(sub_expression[:i])
            right = helper(sub_expression[i + 1 :])
            operator = OPERATION_MAP[sub_expression[i]]
            for x in left:
                for y in right:
                    result.append(operator(x, y))
        return result

    expression = parse_expression(s)
    return helper(expression)


def parse_expression(s: str) -> List[Union[int, str]]:
    result = []
    current = 0
    for char in s + "%":
        if char in string.digits:
            current *= 10
            current += int(char)
        else:
            result.append(current)
            current = 0
            if char != "%":
                result.append(char)
    return result


def main():
    print("Expression evaluations: " + str(diff_ways_to_evaluate_expression("1+2*3")))

    print("Expression evaluations: " + str(diff_ways_to_evaluate_expression("2*3-4-5")))


main()
