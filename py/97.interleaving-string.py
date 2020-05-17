#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start

## 字符串匹配，一般dp二维数组
## dp[i][j] 代表长度为i的s1, 长度为j 的s2
## 递推公式：dp[i][j] = (dp[i - 1][j] && s1[i - 1] == s3[i - 1 + j]) || (dp[i][j - 1] && s2[j - 1] == s3[j - 1 + i]);
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        ## 长度之和不等于s3, 直接返回false
        if m + n != len(s3):
            return False
        dp = [[False for j in range(n+1)] for i in range(m+1)]
        dp[0][0] = True
        ## 若s1和s2其中的一个为空串的话，那么另一个肯定和s3的长度相等，则按位比较
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i][j-1] and s2[j-1] == s3[i+j-1]) \
                    or (dp[i-1][j] and s1[i-1] == s3[i+j-1])
        
        return dp[m][n]


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac" 
print(Solution().isInterleave(s1, s2, s3))

# @lc code=end

