#
# @lc app=leetcode id=134 lang=python3
#
# [134] Gas Station
#

# @lc code=start
from typing import List

## 1、如果整个路程总的油量 gasSum 小于总的耗油量 costSum，则无论从哪个点触发，都铁定无法绕行一周。
# 因此，total < 0时， 返回-1，total >= 0时，则可以跑一圈，寻找可能的i
## 2、有两个点 i1、i2，且是从 i1 驶向 i2，有 sum 表示从 i1 到达 i2 时油箱剩余的油量，此时有 sum ∈ [0, +∞]，
# 当sum + gas[i2] - cost[i2] < 0, 表示从 i2 到下一个点的耗油量太大，根本无法达到。
# 因此，在 [i1, i2] 中的任意一点出发，都无法达到 i2 + 1 这个位置点。

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if not gas or not cost:
            return -1
        sum = total = 0
        index = -1
        for i in range(len(gas)):
            sum += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if sum < 0:
                # 注意，可能的情况是 i2+1，因此这里记录为 i, 会返回 i+1
                index = i
                sum = 0
        if total < 0:
            return -1
        return index + 1

gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(Solution().canCompleteCircuit(gas, cost))
# @lc code=end

