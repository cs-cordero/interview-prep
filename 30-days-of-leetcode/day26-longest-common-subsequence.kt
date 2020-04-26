class Solution {
    fun longestCommonSubsequence(text1: String, text2: String): Int {
        val dp = Array(text1.length + 1) { IntArray(text2.length + 1) }

        for (i in 1..dp.lastIndex) {
            for (j in 1..dp[i].lastIndex) {
                dp[i][j] = maxOf(
                    dp[i - 1][j],
                    dp[i][j - 1],
                    dp[i - 1][j - 1] + if (text1[i - 1] == text2[j - 1]) 1 else 0
                )
            }
        }

        return dp.last().last()
    }
}
