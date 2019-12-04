class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            temp = nums[i]
            nums[i] = None
            while temp is not None:
                if temp == len(nums):
                    break
                temp2 = nums[temp]
                nums[temp] = temp
                temp = temp2

        for i, value in enumerate(nums):
            if value is None:
                return i

        return len(nums)
