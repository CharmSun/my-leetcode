#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
from typing import List

## 循环价格，选取之前的最小买入价格，计算最大利润
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        res = 0
        buy = prices[0]
        for price in prices:
            buy = min(buy, price)
            res = max(res, price - buy)
        return res

input = [7,1,5,3,6,4]
print(Solution().maxProfit(input))
# @lc code=end

