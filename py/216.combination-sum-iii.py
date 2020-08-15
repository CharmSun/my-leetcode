#
# @lc app=leetcode id=216 lang=python3
#
# [216] Combination Sum III
#

# @lc code=start
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def dfs(begin, curAns, curSum):
            if len(curAns) == k and curSum == n:
                res.append(curAns)
                return
            for i in range(begin, 10):
                if curSum + i > n:
                    return
                dfs(i+1, curAns+[i], curSum+i)
        dfs(1, [], 0)
        return res

k = 3
n = 7
print(Solution().combinationSum3(k, n))

# @lc code=end

