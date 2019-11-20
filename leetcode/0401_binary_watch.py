from typing import List


class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        answer = []

        def convert_number_to_time(n: int) -> str:
            hour = n >> 6
            minute = n & ((1 << 6) - 1)
            return f"{hour}:{str(minute).zfill(2)}"

        def helper(n: int, current: int, highest_bit_place: int) -> None:
            if n == 0:
                answer.append(convert_number_to_time(current))
                return None

            for shift in range(highest_bit_place):
                candidate = 1 << shift

                shares_bit_with_current = (candidate & current) == candidate
                if shares_bit_with_current:
                    return None

                candidate |= current
                if (candidate >> 6) >= 12 or (candidate & ((1 << 6) - 1) >= 60):
                    return None
                helper(n - 1, candidate, shift + 1)

        helper(num, 0, 10)
        return answer
