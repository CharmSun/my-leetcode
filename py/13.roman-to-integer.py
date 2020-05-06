#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        i = 0
        dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X':10, 'V': 5, 'I': 1}
        while i < len(s):
            ## 判断类似IV的情况
            if i+1 < len(s) and dict[s[i+1]] > dict[s[i]]:
                res += dict[s[i+1]] - dict[s[i]]
                i += 2
            else:
                res += dict[s[i]]
                i += 1
        return res

print(Solution().romanToInt('MCMXCIV'))        
# @lc code=end

