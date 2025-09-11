"""
Problem: Subarray Sum Equals K
Link: https://leetcode.com/problems/subarray-sum-equals-k/
Difficulty: Medium

Approach:
- Prefix sum + hashmap (freq of prefix sums).
- For each prefix S, subarrays ending here with sum k equal freq[S - k].

Time: O(n)
Space: O(n)
"""

def subarray_sum(nums, k):
    prefix = 0
    freq = {0: 1}
    count = 0
    for x in nums:
        prefix += x
        count += freq.get(prefix - k, 0)
        freq[prefix] = freq.get(prefix, 0) + 1
    return count


if __name__ == "__main__":
    print(subarray_sum([1,1,1], 2))          # 2
    print(subarray_sum([1,2,3], 3))          # 2  -> [1,2], [3]
    print(subarray_sum([1,-1,1,-1], 0))      # 4
    print(subarray_sum([3,4,7,2,-3,1,4,2], 7))  # 4
