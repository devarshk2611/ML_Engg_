"""
Problem: Binary Search
Link: https://leetcode.com/problems/binary-search/
Time: O(log n) | Space: O(1)
"""

def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1

if __name__ == "__main__":
    print(search([-1,0,3,5,9,12], 9))   # 4
    print(search([-1,0,3,5,9,12], 2))   # -1
