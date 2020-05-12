#
# @lc app=leetcode id=44 lang=python3
#
# [44] Wildcard Matching
#

# @lc code=start

## DP算法：
## 1、if p[j-1] == '*'; f(i,j) = f(i,j-1) or f(i-1,j)
## 2、if p[j-1] != '*'; f(i,j) = f(i-1,j-1) and (s[i-1] == p[j-1] or p[j-1] == '?')
## f(i,j)表示输入s[0:i]和输入p[0:j]时的匹配结果

## 非DP如下：
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len, p_len = len(s), len(p)
        i = j = 0 # 记录 s 与 p 的当前匹配位置
        matched_i = 0 # 记录 s 已经匹配的位置
        pos_star = -1 # 记录上一个 * 的位置

        while i < s_len:
            if j < p_len and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            elif j < p_len and p[j] == '*':
                matched_i = i
                pos_star = j
                j += 1
            elif pos_star != -1:
                matched_i += 1
                i = matched_i
                j = pos_star + 1
            else:
                return False
        
        while j < p_len and p[j] == '*':
            j += 1

        return j == p_len

s = "acdcb"
p = "a*c?b"
print(Solution().isMatch(s, p))
        
# @lc code=end

