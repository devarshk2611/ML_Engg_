# LeetCode 9: Palindrome Number
# Time: O(log10(n))
# Space: O(1)

class Solution(object):
    def isPalindrome(self, x):
        # Negative numbers or numbers ending with 0 (except 0) are not palindromes
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        # For even length: x == reversed_half
        # For odd length: x == reversed_half // 10 (ignore middle digit)
        return x == reversed_half or x == reversed_half // 10


if __name__ == "__main__":
    sol = Solution()
    print(sol.isPalindrome(121))    # True
    print(sol.isPalindrome(-121))   # False
    print(sol.isPalindrome(10))     # False
    print(sol.isPalindrome(12321))  # True
