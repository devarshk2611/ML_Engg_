"""
Problem: Insert Interval
Link: https://leetcode.com/problems/insert-interval/
Difficulty: Medium

Approach:
1) Append all intervals that end before new.start.
2) Merge all overlapping intervals into new.
3) Append the remaining intervals.
Time: O(n) | Space: O(n)
"""

def insert_interval(intervals, new):
    res = []
    i, n = 0, len(intervals)
    ns, ne = new

    while i < n and intervals[i][1] < ns:
        res.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= ne:
        ns = min(ns, intervals[i][0])
        ne = max(ne, intervals[i][1])
        i += 1
    res.append([ns, ne])

    while i < n:
        res.append(intervals[i])
        i += 1

    return res


if __name__ == "__main__":
    print(insert_interval([[1,3],[6,9]], [2,5]))                   # [[1,5],[6,9]]
    print(insert_interval([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # [[1,2],[3,10],[12,16]]
    print(insert_interval([], [5,7]))                               # [[5,7]]
    print(insert_interval([[1,5]], [2,3]))                          # [[1,5]]
    print(insert_interval([[1,5]], [2,7]))                          # [[1,7]]
