import string


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        if not target:
            return ""

        board = {
            character: (
                (ord(character) - ord("a")) // 5,
                (ord(character) - ord("a")) % 5,
            )
            for character in string.ascii_lowercase
        }

        def get_path(start: str, end: str) -> str:
            start_row, start_col = board[start]
            end_row, end_col = board[end]

            delta_row = end_row - start_row
            delta_col = end_col - start_col
            vertical = "U" * abs(delta_row) if delta_row < 0 else "D" * delta_row
            horizontal = "L" * abs(delta_col) if delta_col < 0 else "R" * delta_col

            return (
                f"{vertical}{horizontal}!" if end != "z" else f"{horizontal}{vertical}!"
            )

        return "".join(get_path(*values) for values in zip("a" + target[:-1], target))


assert Solution().alphabetBoardPath("leet") == "DDR!UURRR!!DDD!"
assert Solution().alphabetBoardPath("code") == "RR!DDRR!UUL!R!"
