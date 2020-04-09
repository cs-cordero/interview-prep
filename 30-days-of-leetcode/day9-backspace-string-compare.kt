class Solution {
    fun backspaceCompare(S: String, T: String): Boolean {
        // Given two strings S and T, return if they are equal when both are
        // typed into empty text editors. # means a backspace character.

        fun getNextIndex(word: String, index: Int): Int {
            var backspaceCount = 0;
            var i = index;
            while (i >= 0 && (backspaceCount > 0 || word.get(i) == '#')) {
                backspaceCount = if (word.get(i) == '#') ++backspaceCount else --backspaceCount;
                --i;
            }
            return i;
        }

        var s = getNextIndex(S, S.lastIndex);
        var t = getNextIndex(T, T.lastIndex);

        while (s >= 0 && t >= 0 && S.get(s) == T.get(t)) {
            s = getNextIndex(S, s - 1);
            t = getNextIndex(T, t - 1);
        }

        return s == -1 && t == -1;
    }
}
