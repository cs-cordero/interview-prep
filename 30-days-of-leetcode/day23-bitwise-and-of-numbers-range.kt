class Solution {
    fun rangeBitwiseAnd(m: Int, n: Int): Int {
        if (sizeBits(m) < sizeBits(n)) return 0
        return (m..n).fold(m) { result, element -> result and element }
    }

    fun sizeBits(n: Int): Int {
        if (n < 0) return -1
        if (n == 0) return 1
        return (kotlin.math.log(n.toDouble(), 2.0) + 1.0).toInt()
    }
}
