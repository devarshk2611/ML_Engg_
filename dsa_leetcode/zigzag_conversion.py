class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row = 0
        direction = -1  # -1 means up, +1 means down

        for ch in s:
            rows[curr_row] += ch

            # Change direction at top or bottom
            if curr_row == 0 or curr_row == numRows - 1:
                direction *= -1

            curr_row += direction

        return "".join(rows)


if __name__ == "__main__":
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 3))  # PAHNAPLSIIGYIR
    print(sol.convert("PAYPALISHIRING", 4))  # PINALSIGYAHRPI
