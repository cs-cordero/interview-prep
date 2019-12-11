from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        current_state = 0
        for cell in cells:
            current_state <<= 1
            current_state |= cell

        memo = []
        for iterations in range(1, N + 1):
            next_state = 0
            binary = "{0:b}".format(current_state).zfill(len(cells))
            for i in range(len(binary)):
                next_state <<= 1

                if i == 0 or i == len(binary) - 1:
                    next_state |= 0
                else:
                    left = binary[i - 1]
                    right = binary[i + 1]
                    next_state |= 1 if left == right else 0
            if memo and next_state == memo[0]:
                break
            current_state = next_state
            memo.append(next_state)

        remaining_iterations = N - len(memo)
        i = len(memo) - 1
        current_state = memo[(i + remaining_iterations) % len(memo)]
        return list(map(int, "{0:b}".format(current_state).zfill(len(cells))))
