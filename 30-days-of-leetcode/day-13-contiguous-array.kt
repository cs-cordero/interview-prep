class Solution {
    fun findMaxLength(nums: IntArray): Int {
        // Given a binary array, find the maximum length of a contiguous
        // subarray with equal number of 0 and 1.

        val counts = mutableMapOf<Int, MutableList<Int>>(0 to mutableListOf(0))
        var count = 0
        nums.forEachIndexed { i, num ->
            count += if (num == 1) 1 else -1
            if (!counts.containsKey(count)) {
                counts[count] = mutableListOf()
            }
            counts[count]?.add(i + 1)
        }

        return counts.flatMap { (_, it) -> listOf<Int>(it.last() - it.first()) }.max() ?: 0
    }
}
