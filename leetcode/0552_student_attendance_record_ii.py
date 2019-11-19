class Solution:
    def checkRecord(self, n: int) -> int:
        total = 3
        single_l = 1
        double_l = 0

        pure_count = 2
        pure_single_l = 1
        pure_double_l = 0

        M = 10 ** 9 + 7

        if n <= 0:
            return 0
        elif n == 1:
            return total

        for i in range(2, n + 1):
            prev_pure_count = pure_count
            prev_pure_single_l = pure_single_l
            prev_pure_double_l = pure_double_l
            pure_count = (prev_pure_count + prev_pure_count - prev_pure_double_l) % M
            pure_single_l = prev_pure_count - prev_pure_double_l - prev_pure_single_l
            pure_double_l = prev_pure_single_l

            prev_total = total
            prev_single_l = single_l
            prev_double_l = double_l
            double_l = prev_single_l
            single_l = prev_total - prev_double_l - prev_single_l
            total = (prev_total + prev_total - prev_double_l + prev_pure_count) % M
        return total
