from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        i = 0
        while i < len(nums):
            if nums[i] != i + 1:
                temp, nums[i] = nums[i], None
                while True:
                    if nums[temp - 1] == temp:
                        result.append(temp)
                        break
                    elif nums[temp - 1] is None:
                        nums[temp - 1] = temp
                        break

                    swap_helper = nums[temp - 1]
                    nums[temp - 1] = temp
                    temp = swap_helper
            i += 1
        return result
