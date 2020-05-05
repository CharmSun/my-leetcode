#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
## ss 存每行字符
## 偶数列正向，奇数列反向
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1: 
            return s
        ss = ['' for i in range(numRows)]
        for i in range(len(s)):
            col = i // (numRows - 1)
            mod = i % (numRows - 1)
            if col % 2 == 1 :
                ss[numRows - 1 - mod] += s[i]
            else:
                ss[mod] += s[i]
        res = ''
        for i in range(numRows):
            res += ss[i]
        return res
        
# @lc code=end

