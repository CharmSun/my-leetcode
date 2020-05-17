#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start

## 使用DP， 根据前两个数字，分情况判断dp[i], i为当前字符串长度
class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        if n == 1:
            return 1
        dp = [0] * (n + 1)
        dp[1] = 1
        start = int(s[0:2])
        if start <= 26 and start % 10 != 0: 
            dp[2] = 2
        elif (start > 26 and start % 10 != 0) or start == 10 or start == 20:
            dp[2] = 1
        for i in range(3, n+1):
            sub = int(s[i-2:i])
            if (sub > 0 and sub < 10) or (sub > 26 and sub % 10 != 0):
                dp[i] = dp[i-1]
            elif sub > 10 and sub <= 26 and sub != 20:
                dp[i] = dp[i-2] + dp[i-1]
            elif sub == 10 or sub == 20:
                dp[i] = dp[i-2]
            else:
                dp[i] = 0
        return dp[n]
            
print(Solution().numDecodings('227'))
        
# @lc code=end

