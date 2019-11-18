from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def can_ship(capacity: int) -> bool:
            days_required = 0
            current_capacity = 0
            for weight in weights:
                if current_capacity + weight <= capacity:
                    current_capacity += weight
                else:
                    current_capacity = weight
                    days_required += 1
                    if days_required >= D:
                        return False
            days_required += 1 if current_capacity else 0
            return days_required <= D

        left = max(weights)
        right = sum(weights) + 1
        while left < right:
            mid = (left + right) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left
