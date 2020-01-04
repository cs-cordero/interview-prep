from collections import defaultdict
from typing import Iterable, Union


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        counts = defaultdict(int)
        stack = []
        parsed = list(parse_formula(formula))
        i = 0
        while i < len(parsed):
            if parsed[i] == "(":
                stack.append(counts)
                counts = defaultdict(int)
                i += 1
            elif parsed[i] == ")":
                group_freq = parsed[i + 1]
                for number in counts:
                    counts[number] *= group_freq
                for number, freq in stack.pop().items():
                    counts[number] += freq
                i += 2
            elif parsed[i].isalpha():
                if i + 1 < len(parsed) and isinstance(parsed[i + 1], int):
                    counts[parsed[i]] += parsed[i + 1]
                    i += 2
                else:
                    counts[parsed[i]] += 1
                    i += 1
            else:
                assert False, f"Invariant. {formula[i]}"
        result = []
        for molecule, freq in sorted(counts.items()):
            if freq == 1:
                result.append(molecule)
            elif freq > 1:
                result.append(f"{molecule}{freq}")
        return "".join(result)


def parse_formula(formula: str) -> Iterable[Union[str, int]]:
    i = 0
    while i < len(formula):
        if formula[i] in ("(", ")"):
            yield formula[i]
            i += 1
        elif formula[i].isdigit():
            number = 0
            while i < len(formula) and formula[i].isdigit():
                number *= 10
                number += int(formula[i])
                i += 1
            yield number
        elif formula[i].isalpha():
            molecule = formula[i]
            i += 1
            while i < len(formula) and formula[i].isalpha() and formula[i].islower():
                molecule += formula[i]
                i += 1
            yield molecule
        else:
            assert False, f"Invariant. {formula[i]}"
