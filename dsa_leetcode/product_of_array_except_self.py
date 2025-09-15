"""
Problem: Product of Array Except Self
Link: https://leetcode.com/problems/product-of-array-except-self/
Difficulty: Medium

Approach:
- res[i] = product of all elements to the left of i
- Then multiply by product of all elements to the right of i (tracked with a running variable)
- No division; two passes.

Time: O(n)
Space: O(1) extra (excluding output)
"""

def product_except_self(nums):
    n = len(nums)
    res = [1] * n

    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]

    return res


if __name__ == "__main__":
    print(product_except_self([1,2,3,4]))     # [24,12,8,6]
    print(product_except_self([-1,1,0,-3,3])) # [0,0,9,0,0]
    print(product_except_self([2,2]))         # [2,2]
