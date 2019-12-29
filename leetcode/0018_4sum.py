from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        quadruplets = []
        if len(nums) < 4:
            return quadruplets

        nums.sort()
        a = 0
        while a < len(nums) - 3:
            b = a + 1
            while b < len(nums) - 2:
                c = b + 1
                d = len(nums) - 1
                while c < d:
                    current = nums[a] + nums[b] + nums[c] + nums[d]
                    if current == target:
                        quadruplets.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    elif current > target:
                        d -= 1
                    else:
                        c += 1
                b += 1
                while b < len(nums) - 2 and nums[b] == nums[b - 1]:
                    b += 1
            a += 1
            while a < len(nums) - 3 and nums[a] == nums[a - 1]:
                a += 1

        return quadruplets
