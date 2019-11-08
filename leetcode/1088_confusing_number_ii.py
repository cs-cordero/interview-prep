from collections import deque


class Solution:
    def confusingNumberII(self, N: int) -> int:
        valid = {0, 1, 6, 8, 9}
        change_map = {
            0: 0,
            1: 1,
            6: 9,
            8: 8,
            9: 6,
        }

        count = 0

        queue = deque((number, str(change_map[number])) for number in valid if number)
        while queue:
            value, rotated = queue.popleft()
            for num in valid:
                next_num = (value * 10) + num
                if next_num > N:
                    continue

                next_rotated = str(change_map[num]) + rotated
                queue.append((next_num, next_rotated))

            if value != int(rotated):
                count += 1

        return count


print(Solution().confusingNumberII(20))
print(Solution().confusingNumberII(100))
print(Solution().confusingNumberII(1000000000))
