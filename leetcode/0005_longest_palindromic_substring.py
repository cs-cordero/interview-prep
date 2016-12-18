class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        longest_palindrome = ""

        for i in range(len(s) - 1):
            double_palindrome = (
                self.get_palindrome(s, i, i + 1) if s[i] == s[i + 1] else ""
            )
            single_palindrome = self.get_palindrome(s, i, i)

            current_palindrome = (
                double_palindrome
                if len(double_palindrome) > len(single_palindrome)
                else single_palindrome
            )

            if len(current_palindrome) > len(longest_palindrome):
                longest_palindrome = current_palindrome
        return longest_palindrome

    def get_palindrome(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left] if left == right else s[left + 1 : right]


assert Solution().longestPalindrome("") == ""
assert Solution().longestPalindrome("a") == "a"
assert Solution().longestPalindrome("ab") == "a"
assert Solution().longestPalindrome("aa") == "aa"
assert Solution().longestPalindrome("abcba") == "abcba"
assert Solution().longestPalindrome("bbbb") == "bbbb"
assert Solution().longestPalindrome("bbbbbb") == "bbbbbb"
assert Solution().longestPalindrome("gfabcbafh") == "fabcbaf"
assert Solution().longestPalindrome("gfabcbafh") == "fabcbaf"
