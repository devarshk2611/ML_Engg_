# LeetCode 394: Decode String
# Time: O(n)
# Space: O(n)

class Solution(object):
    def decodeString(self, s):
        stack = []
        curr = ""
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                stack.append((curr, num))
                curr = ""
                num = 0

            elif ch == ']':
                prev, k = stack.pop()
                curr = prev + curr * k

            else:
                curr += ch

        return curr


if __name__ == "__main__":
    sol = Solution()
    print(sol.decodeString("3[a]2[bc]"))      # aaabcbc
    print(sol.decodeString("3[a2[c]]"))       # accaccacc
    print(sol.decodeString("2[abc]3[cd]ef"))  # abcabccdcdcdef
    print(sol.decodeString("10[a]"))          # aaaaaaaaaa
