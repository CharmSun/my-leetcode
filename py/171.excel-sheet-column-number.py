#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        dict = {}
        for i in range(26):
            dict[chr(ord('A') + i)] = i + 1
        res = 0
        for i in range(0, len(s)):
            res = res * 26 + dict[s[i]]
        return res

print(Solution().titleToNumber("A"))
        
# @lc code=end

