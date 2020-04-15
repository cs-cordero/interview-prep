fun productExceptSelf(nums: IntArray): IntArray {
    val result = IntArray(nums.size, { 1 })

    // go forward
    var product = 1
    nums.forEachIndexed { index, value ->
        result[index] *= product
        product *= value
    }

    // go backward
    product = 1
    nums.indices.reversed().forEach {
        result[it] *= product
        product *= nums[it]
    }

    return result
}
