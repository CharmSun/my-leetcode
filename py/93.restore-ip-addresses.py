#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#

# @lc code=start
from typing import List

## 回溯
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        output = []
        self.dfs(s, [], output)
        return output
    
    def dfs(self, s, ans, output):
        ## 满足结果条件
        if len(s) == 0 and len(ans) == 4:
            output.append('.'.join([str(i) for i in ans]))
        if len(s) > 0 and len(ans) < 4:
            n = min(len(s), 3)
            for i in range(1, n+1):
                p = int(s[0:i])
                ## 0~255，并且没有前置0
                if p >= 0 and p <= 255 and len(str(p)) == i:
                    ans.append(p)
                    self.dfs(s[i:], ans, output)
                    ans.pop()

input = "25525511135"
print(Solution().restoreIpAddresses(input))

# @lc code=end

