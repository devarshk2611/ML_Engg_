# LeetCode 84: Largest Rectangle in Histogram
# Time: O(n)
# Space: O(n)

class Solution(object):
    def largestRectangleArea(self, heights):
        # Append sentinel to flush stack at the end
        heights.append(0)

        stack = []  # stores indices with increasing heights
        best = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                top = stack.pop()
                height = heights[top]

                left_smaller_index = stack[-1] if stack else -1
                width = i - left_smaller_index - 1

                best = max(best, height * width)

            stack.append(i)

        heights.pop()  # restore input
        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # 10
    print(sol.largestRectangleArea([2, 4]))              # 4
    print(sol.largestRectangleArea([1, 1, 1, 1]))        # 4
    print(sol.largestRectangleArea([0, 9]))              # 9
