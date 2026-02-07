# LeetCode 16: 3Sum Closest
# Time: O(n^2)
# Space: O(1) extra (sorting aside)

class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)

        best = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            # Optional skip duplicates for i (not required for correctness, helps speed)
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if abs(s - target) < abs(best - target):
                    best = s

                if s == target:
                    return s
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return best


if __name__ == "__main__":
    sol = Solution()
    print(sol.threeSumClosest([-1, 2, 1, -4], 1))  # 2
    print(sol.threeSumClosest([0, 0, 0], 1))       # 0
    print(sol.threeSumClosest([1, 1, 1, 1], 0))    # 3
