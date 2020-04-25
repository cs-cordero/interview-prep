class Solution {
    fun canJump(nums: IntArray): Boolean {
        // Given an array of non-negative integers, you are initially positioned at the first index of the array.
        // Each element in the array represents your maximum jump length at that position.
        // Determine if you are able to reach the last index.
        var furthestIndex = 0
        nums.forEachIndexed { index, jumpSize ->
            if (index > furthestIndex) return false
            furthestIndex = Math.max(furthestIndex, index + jumpSize)
        }
        return true
    }
}
