#
# @lc app=leetcode id=32 lang=python3
#
# [32] Longest Valid Parentheses
#

# @lc code=start

## 1、s[i] == ')' and s[i-1] =='(' ,如 ".......()", => dp[i] = dp[i-2] + 2
## 2、s[i] == ')' and s[i-1] ==')'，如 ".......))", 如果 s[i - dp[i-1] - 1] == '(', 则 dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxLen = 0
        dp = [0] * len(s)
        for i in range(1, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2 if i >=2 else 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':
                    if i - dp[i-1] >= 2:
                        dp[i] = dp[i-1] + 2 + dp[i - dp[i-1] - 2]
                    else:
                        dp[i] = dp[i-1] + 2
                maxLen = max(maxLen, dp[i])
        return maxLen
        
# @lc code=end

