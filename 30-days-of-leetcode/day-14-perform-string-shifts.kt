class Solution {
    fun stringShift(s: String, shift: Array<IntArray>): String {
        if (s.isNullOrEmpty()) {
            return s
        }

        val start = shift.fold(0) { acc, it ->
            val direction = if (it.component1() == 0) 1 else -1
            (acc + direction * it.component2() + s.length) % s.length
        }

        fun rotate(s: String, i: Int): String {
            if (!s.indices.contains(i)) {
                return s
            }

            val right = s.substring(IntRange(i, s.lastIndex))
            val left = (if (i - 1 >= 0) i - 1 else null)?.let {
                s.substring(IntRange(0, it))
            } ?: ""
            return "$right$left"
        }

        return rotate(s, start)
    }
}
