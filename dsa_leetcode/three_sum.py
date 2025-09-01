"""
Problem: 3Sum
Link: https://leetcode.com/problems/3sum/
Difficulty: Medium

Approach:
- Sort the array
- Fix i; use two pointers l, r to find pairs that sum to -nums[i]
- Skip duplicates at i, l, r to keep triplets unique

Time: O(n^2)
Space: O(1) extra (excluding output)
"""
def three_sum(nums):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        target = -nums[i]
        l, r = i + 1, n - 1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                res.append([nums[i], nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while l < r and nums[r] == nums[r + 1]:
                    r -= 1
            elif s < target:
                l += 1
            else:
                r -= 1
    return res

if __name__ == "__main__":
    print(three_sum([-1,0,1,2,-1,-4]))  # [[-1,-1,2], [-1,0,1]]
    print(three_sum([0,0,0,0]))         # [[0,0,0]]
    print(three_sum([1,2,-2,-1]))       # []
