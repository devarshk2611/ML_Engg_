from collections import Counter
import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return [num for num, freq in heapq.nlargest(k, count.items(), key=lambda x: x[1])]


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1,1,1,2,2,3], 2))  # Expected [1,2]
    print(sol.topKFrequent([1], 1))            # Expected [1]
