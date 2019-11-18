from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        return ",".join(
            value.replace("\\", "\\\\").replace(",", "\,")  # noqa: W605
            if value
            else '""'
            for value in strs
        )

    def decode(self, s: str) -> List[str]:
        result = []

        escaped = False
        current = ""
        for character in s:
            if character == "\\" and not escaped:
                escaped = True
                continue
            elif character == "," and not escaped:
                current = "" if current == '""' else current
                result.append(current)
                current = ""
            else:
                current += character
            escaped = False
        if current:
            current = "" if current == '""' else current
            result.append(current)
        return result
