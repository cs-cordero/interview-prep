class FirstUnique(nums: IntArray) {
    private var index: Int = 0
    private val uniqueAddedInts = mutableListOf<Int>()
    private val freqs = mutableMapOf<Int, Int>()

    init {
        nums.forEach { add(it) }
    }

    fun showFirstUnique(): Int = uniqueAddedInts.getOrElse(index, { -1 })

    fun add(value: Int) {
        if (!freqs.containsKey(value)) {
            uniqueAddedInts.add(value)
        }

        freqs[value] = freqs.getOrPut(value, { 0 }) + 1
        while (
            index < uniqueAddedInts.size &&
            uniqueAddedInts[index]?.let { freqs[it] }?.let { it > 1 } ?: false
        ) {
            index += 1
        }
    }
}
