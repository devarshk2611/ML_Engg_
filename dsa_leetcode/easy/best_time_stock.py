"""
Problem: Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Difficulty: Easy

Approach:
- Track the minimum price so far.
- For each price, calculate profit if sold today.
- Update maximum profit if higher.

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_profit:
                max_profit = price - min_price

        return max_profit


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))  # 5
    print(sol.maxProfit([7,6,4,3,1]))    # 0
