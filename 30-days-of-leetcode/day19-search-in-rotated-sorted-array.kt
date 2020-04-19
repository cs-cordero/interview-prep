class Solution {
    fun search(nums: IntArray, target: Int): Int {
        // Suppose an array sorted in ascending order is rotated at some pivot
        // unknown to you beforehand.
        // (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
        //
        // You are given a target value to search. If found in the array return
        // its index, otherwise return -1.
        //
        // You may assume no duplicate exists in the array.
        // Your algorithm's runtime complexity must be in the order of O(log n).
        var left = 0
        var right = nums.lastIndex

        while (left <= right) {
            val midpoint = (left + right) / 2
            val value = nums[midpoint]

            when {
                value == target -> return midpoint
                value > target -> {
                    if (value <= nums[right] || target >= nums[left]) {
                        right = midpoint - 1
                    } else {
                        left = midpoint + 1
                    }
                }
                value < target -> {
                    if (value >= nums[left] || target <= nums[right]) {
                        left = midpoint + 1
                    } else {
                        right = midpoint - 1
                    }
                }
            }
        }
        return -1
    }
}
