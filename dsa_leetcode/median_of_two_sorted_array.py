# LeetCode 4: Median of Two Sorted Arrays
# Time: O(log(min(m, n)))
# Space: O(1)

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        m, n = len(A), len(B)

        # Ensure A is the smaller array
        if m > n:
            A, B, m, n = B, A, n, m

        total = m + n
        half = (total + 1) // 2

        l, r = 0, m

        while l <= r:
            i = (l + r) // 2
            j = half - i

            A_left = A[i - 1] if i > 0 else float("-inf")
            A_right = A[i] if i < m else float("inf")
            B_left = B[j - 1] if j > 0 else float("-inf")
            B_right = B[j] if j < n else float("inf")

            if A_left <= B_right and B_left <= A_right:
                # Correct partition
                if total % 2 == 1:
                    return max(A_left, B_left)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2.0
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1

        # Should never reach here
        return 0.0


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))        # 2.0
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))     # 2.5
    print(sol.findMedianSortedArrays([0, 0], [0, 0]))     # 0.0
    print(sol.findMedianSortedArrays([], [1]))            # 1.0
