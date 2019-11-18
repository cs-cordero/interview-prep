from typing import Iterable, List, Set


class Solution:
    def expand(self, S: str) -> List[str]:
        delimiters = {"{", "}", ","}

        def get_tokens() -> Iterable[Set[str]]:
            token = ""

            i = 0
            while i < len(S):
                character = S[i]
                if character not in delimiters:
                    token += character
                else:
                    yield {token}
                    token = ""

                    assert character == "{"

                    j = i
                    grouping = ""
                    while j < len(S):
                        grouping += S[j]
                        if S[j] == "}":
                            break
                        j += 1
                    yield set(grouping[1:-1].split(","))

                    i = j
                i += 1
            if token:
                yield {token}

        result = None
        for token in get_tokens():
            if result is None:
                result = token
                continue

            result = {f"{x}{y}" for x in result for y in token}
        return sorted(result)
