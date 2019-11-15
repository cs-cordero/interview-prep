class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        def find_palindrome(left: int, right: int) -> str:
            if s[left] != s[right]:
                return ""

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1 : right]

        best_palindrome = s[0]
        for i, value in enumerate(s[1:], 1):
            for args in [(i, i), (i - 1, i)]:
                palindrome = find_palindrome(*args)
                if len(palindrome) > len(best_palindrome):
                    best_palindrome = palindrome
        return best_palindrome
