class Solution(object):
    def maxProduct(self, nums):
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]

            # swap when current number is negative
            if curr < 0:
                max_prod, min_prod = min_prod, max_prod

            max_prod = max(curr, max_prod * curr)
            min_prod = min(curr, min_prod * curr)

            result = max(result, max_prod)

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProduct([2,3,-2,4]))     # Expected: 6
    print(sol.maxProduct([-2,0,-1]))      # Expected: 0
    print(sol.maxProduct([-2,3,-4]))      # Expected: 24
