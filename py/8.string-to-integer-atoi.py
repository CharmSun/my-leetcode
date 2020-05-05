#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start

## 正则表达式
import re

class Solution:
    def myAtoi(self, str: str) -> int:
        INT_MAX = 2 ** 31 -1
        INT_MIN = - 2 ** 31
        match = re.match(r'^[+-]?\d+', str.strip())
        if match:
            numStr = match.group()
            num = int(numStr)
            if num > INT_MAX:
                return INT_MAX
            if num < INT_MIN:
                return INT_MIN
            return num
        return 0
        
# @lc code=end

