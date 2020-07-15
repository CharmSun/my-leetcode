#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#

# @lc code=start

from typing import List

## 1、dp[i]表示[0, i] 子串是否能够由wordDict组成
## 2、dp[i] = 对于任意j, dp[j] && wordDict 包含 s[j + 1, i]，其中j 属于区间 [0, i] 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        wordSet = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]

s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
print(Solution().wordBreak(s, wordDict))    

# @lc code=end

