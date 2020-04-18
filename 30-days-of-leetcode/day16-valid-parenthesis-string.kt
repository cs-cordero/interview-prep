class Solution {
    fun checkValidString(s: String): Boolean {
        //  Given a string containing only three types of characters: '(', ')'
        //  and '*', write a function to check whether this string is valid. We
        //  define the validity of a string by these rules:
        //
        // Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        // Any right parenthesis ')' must have a corresponding left parenthesis '('.
        // Left parenthesis '(' must go before the corresponding right parenthesis ')'.
        // '*' could be treated as a single right parenthesis ')' or a single
        // left parenthesis '(' or an empty string.
        // An empty string is also valid.

        val memo = mutableMapOf<Pair<Int, Int>, Boolean>()

        fun helper(index: Int, parenthesesDelta: Int): Boolean {
            // base case
            if (parenthesesDelta < 0) return false
            val char = s.getOrNull(index) ?: return parenthesesDelta == 0

            // memoized recursive case
            val memoKey = Pair(index, parenthesesDelta)
            memo[memoKey] = memo.get(memoKey) ?: when (char) {
                '(' -> helper(index + 1, parenthesesDelta + 1)
                ')' -> helper(index + 1, parenthesesDelta - 1)
                '*' -> listOf(
                        Pair(index + 1, parenthesesDelta + 1),
                        Pair(index + 1, parenthesesDelta - 1),
                        Pair(index + 1, parenthesesDelta)
                    ).any { helper(it.first, it.second) }
                else -> throw Exception("Invariant")
            }
            return memo.getValue(memoKey)
        }

        return helper(0, 0)
    }
}
