from collections import Counter

class Solution(object):
    def leastInterval(self, tasks, n):
        if n == 0:
            return len(tasks)

        freq = Counter(tasks)
        maxFreq = max(freq.values())
        maxCount = sum(1 for v in freq.values() if v == maxFreq)

        min_len = (maxFreq - 1) * (n + 1) + maxCount
        return max(len(tasks), min_len)


if __name__ == "__main__":
    sol = Solution()
    print(sol.leastInterval(["A","A","A","B","B","B"], 2))  # 8
    print(sol.leastInterval(["A","A","A","B","B","B"], 0))  # 6
    print(sol.leastInterval(["A","A","A","A","B","B","C","C"], 2))  # 10
