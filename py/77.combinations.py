#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#

# @lc code=start
from typing import List

## 回溯：注意不重复
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        output = []
        def backtrack(ans, num):
            if len(ans) == k:
                output.append(ans)
            elif len(ans) < k:
                for i in range(num, n):
                    backtrack(ans+[i+1], i+1)
        backtrack([], 0)
        return output

n = 4
k = 2                
print(Solution().combine(n, k))
        
# @lc code=end

