"""
Problem: Merge Intervals
Link: https://leetcode.com/problems/merge-intervals/
Difficulty: Medium

Approach:
- Sort by start time.
- If current interval overlaps with last merged (curr.start <= last.end),
  extend last.end = max(last.end, curr.end); otherwise append a new interval.

Time Complexity: O(n log n)  (sorting dominates)
Space Complexity: O(n)  (result list)
"""

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []
    for start, end in intervals:
        if not merged or start > merged[-1][1]:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


if __name__ == "__main__":
    print(merge_intervals([[1,3],[2,6],[8,10],[15,18]]))  # [[1,6],[8,10],[15,18]]
    print(merge_intervals([[1,4],[4,5]]))                  # [[1,5]]
    print(merge_intervals([[1,4],[2,3]]))                  # [[1,4]]
    print(merge_intervals([[1,4],[0,2],[3,5]]))            # [[0,5]]
