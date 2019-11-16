from typing import Iterable, List, Set


class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        stack = []
        delimiters = {"{", "}", ","}

        def get_tokens() -> Iterable[str]:
            current = ""
            for character in expression:
                if character not in delimiters:
                    current += character
                else:
                    if current:
                        yield current
                        current = ""
                    yield character
            if current:
                yield current

        def union_until_open_bracket(current: Set[str]) -> Set[str]:
            while stack and stack[-1] != "{":
                if stack[-1] == ",":
                    stack.pop()
                    continue
                current |= stack.pop()
            if stack:
                stack.pop()  # Drop the "{"
            return current

        def product_until_delimiter(current: Set[str]) -> Set[str]:
            while stack and stack[-1] not in delimiters:
                current = {f"{x}{y}" for x in stack.pop() for y in current}
            return current

        for token in get_tokens():
            if token in delimiters and token != "}":
                stack.append(token)

            elif token == "}":
                most_recent = stack.pop()
                current = set() if most_recent in delimiters else most_recent
                current = union_until_open_bracket(current)
                current = product_until_delimiter(current)
                stack.append(current)

            else:
                current = product_until_delimiter({token})
                stack.append(current)

        return sorted(union_until_open_bracket(set()))
