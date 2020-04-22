class Solution {
    fun subarraySum(nums: IntArray, k: Int): Int {
        // Given an array of integers and an integer k, you need to find the
        // total number of continuous subarrays whose sum equals to k.
        var result = 0

        val freqsSeen = mutableMapOf<Int, Int>(0 to 1).withDefault({ 0 })
        var currentSum = 0
        nums.forEach {
            currentSum += it
            val neededSeen = currentSum - k
            freqsSeen.get(neededSeen)?.also { result += it }
            freqsSeen[currentSum] = freqsSeen.getValue(currentSum) + 1
        }
        return result
    }
}
