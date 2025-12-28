class Solution(object):
    def maxSubarraySumCircular(self, nums):
        # Kadane for max subarray sum
        def kadane_max(arr):
            best = curr = arr[0]
            for x in arr[1:]:
                curr = max(x, curr + x)
                best = max(best, curr)
            return best

        # Kadane for min subarray sum
        def kadane_min(arr):
            best = curr = arr[0]
            for x in arr[1:]:
                curr = min(x, curr + x)
                best = min(best, curr)
            return best

        total = sum(nums)
        max_normal = kadane_max(nums)
        min_normal = kadane_min(nums)

        # If all numbers are negative, max_normal is the answer
        if max_normal < 0:
            return max_normal

        # Best circular = total - min_subarray
        return max(max_normal, total - min_normal)


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubarraySumCircular([1, -2, 3, -2]))      # Expected 3
    print(sol.maxSubarraySumCircular([5, -3, 5]))          # Expected 10
    print(sol.maxSubarraySumCircular([-3, -2, -3]))        # Expected -2
