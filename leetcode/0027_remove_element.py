from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        swap_point = len(nums) - 1

        def move_swap_point() -> None:
            nonlocal swap_point

            while swap_point >= 0 and nums[swap_point] == val:
                nums[swap_point] = None
                swap_point -= 1

        i = 0
        move_swap_point()
        while i < swap_point:
            if nums[i] == val:
                nums[i], nums[swap_point] = nums[swap_point], nums[i]
                move_swap_point()
            i += 1
        return swap_point + 1
