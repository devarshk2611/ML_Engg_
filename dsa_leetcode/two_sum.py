"""
Problem: Two Sum
Link: https://leetcode.com/problems/two-sum/
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution(object):
    def twoSum(self, nums, target):
        idx = {}
        for i, x in enumerate(nums):
            need = target - x
            if need in idx:
                return [idx[need], i]
            idx[x] = i

if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # [0, 1]