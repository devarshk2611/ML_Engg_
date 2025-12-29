class Solution(object):
    def findDuplicate(self, nums):
        slow = nums[0]
        fast = nums[0]

        # Phase 1: detect cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: find entrance to cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


if __name__ == "__main__":
    sol = Solution()
    print(sol.findDuplicate([1,3,4,2,2]))  # Expected: 2
    print(sol.findDuplicate([3,1,3,4,2]))  # Expected: 3
