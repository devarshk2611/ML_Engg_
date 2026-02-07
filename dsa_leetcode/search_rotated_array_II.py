class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return True

            # Case where duplicates prevent us from deciding
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
                continue

            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False


if __name__ == "__main__":
    sol = Solution()
    print(sol.search([2,5,6,0,0,1,2], 0))  # True
    print(sol.search([2,5,6,0,0,1,2], 3))  # False
    print(sol.search([1,1,1,1,1], 2))      # False
    print(sol.search([1,0,1,1,1], 0))      # True
