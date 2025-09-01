"""
File: list_ops.py
Description:
Utility functions for list operations.
Shows ability to manipulate data structures in Python.
"""

def list_summary(nums):
    return {
        "sum": sum(nums),
        "min": min(nums),
        "max": max(nums),
        "unique": list(set(nums))
    }

def second_largest(nums):
    unique_sorted = sorted(set(nums))
    return unique_sorted[-2] if len(unique_sorted) >= 2 else None

def rotate_list(nums, k):
    k = k % len(nums)
    return nums[-k:] + nums[:-k]

if __name__ == "__main__":
    nums = [1, 2, 2, 3, 4, 5]
    print(list_summary(nums))      
    # {'sum': 17, 'min': 1, 'max': 5, 'unique': [1, 2, 3, 4, 5]}

    print(second_largest(nums))    # 4
    print(rotate_list(nums, 2))    # [4, 5, 1, 2, 2, 3]
