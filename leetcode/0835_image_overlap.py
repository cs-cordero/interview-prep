from typing import List


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        a_bits = {
            (row_i, col_i)
            for row_i, row in enumerate(A)
            for col_i, bit in enumerate(row)
            if bit
        }
        b_bits = {
            (row_i, col_i)
            for row_i, row in enumerate(B)
            for col_i, bit in enumerate(row)
            if bit
        }

        translation_deltas_seen = set()
        result = 0
        for row_a, col_a in a_bits:
            for row_b, col_b in b_bits:
                delta = (row_b - row_a, col_b - col_a)
                if delta not in translation_deltas_seen:
                    translation_deltas_seen.add(delta)
                    del_row, del_col = delta
                    result = max(
                        result,
                        sum((r + del_row, c + del_col) in b_bits for r, c in a_bits),
                    )
        return result
