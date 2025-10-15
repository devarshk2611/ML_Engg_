class Solution(object):
    def longestPalindrome(self, s):
        def expand(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l + 1:r]

        res = ""
        for i in range(len(s)):
            # Odd-length palindrome
            tmp = expand(i, i)
            if len(tmp) > len(res):
                res = tmp

            # Even-length palindrome
            tmp = expand(i, i + 1)
            if len(tmp) > len(res):
                res = tmp

        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("babad"))  # Expected "bab" or "aba"
    print(sol.longestPalindrome("cbbd"))   # Expected "bb"
