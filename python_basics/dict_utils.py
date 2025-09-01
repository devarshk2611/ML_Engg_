"""
File: dict_utils.py
Description:
Utility functions for working with Python dictionaries.
"""

def invert_dict(d):
    """Swap keys and values in a dictionary"""
    return {v: k for k, v in d.items()}

def merge_dicts(d1, d2):
    """Merge two dicts (values from d2 override d1 if same key)"""
    return {**d1, **d2}

def frequency_count(items):
    """Count frequency of items in a list"""
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

if __name__ == "__main__":
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    print(invert_dict(d1))                 # {1: 'a', 2: 'b'}
    print(merge_dicts(d1, d2))             # {'a': 1, 'b': 3, 'c': 4}
    print(frequency_count(["apple", "apple", "banana", "apple", "banana"]))
    # {'apple': 3, 'banana': 2}
