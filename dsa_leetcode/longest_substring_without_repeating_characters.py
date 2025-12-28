class Solution(object):
    def lengthOfLongestSubstring(self, s):
        seen = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            # Shrink window until duplicate is removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLongestSubstring("abcabcbb"))  # Expected: 3
    print(sol.lengthOfLongestSubstring("bbbbb"))     # Expected: 1
    print(sol.lengthOfLongestSubstring("pwwkew"))    # Expected: 3
    print(sol.lengthOfLongestSubstring(""))          # Expected: 0
