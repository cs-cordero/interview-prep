class Solution:
    def nextClosestTime(self, time: str) -> str:
        a, b, c, d = map(int, time.replace(":", ""))

        min_abcd = min(a, b, c, d)

        min_abc = min(value if value > d else 10 for value in (a, b, c))
        if min_abc < 10:
            return f"{a}{b}:{c}{min_abc}"

        min_abd = min(value if value > c and value <= 5 else 10 for value in (a, b, d))
        if min_abd < 10:
            return f"{a}{b}:{min_abd}{min_abcd}"

        max_allowed_b = 9 if a < 2 else 3
        min_acd = min(
            value if value > b and value <= max_allowed_b else 10 for value in (a, c, d)
        )
        if min_acd < 10:
            return f"{a}{min_acd}:{min_abcd}{min_abcd}"

        return f"{min_abcd}{min_abcd}:{min_abcd}{min_abcd}"
