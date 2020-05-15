#
# @lc app=leetcode id=65 lang=python3
#
# [65] Valid Number
#

# @lc code=start
import re

## 注意考虑各种不同情况
## 此题没意思，用最简单的方式，正则来吧
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        if not s:
            return False
        regex = r'^[-+]?(\d+\.?|\.\d+)\d*(e[-+]?\d+)?$'
        if re.match(regex, s):
        	return True
        return False

s1 = "0"; # True
s2 = " 0.1 "; # True
s3 = "abc"; # False
s4 = "1 a"; # False
s5 = "2e10"; # True
s6 = "-e10"; # False
s7 = " 2e-9 "; # True
s8 = "+e1"; # False
s9 = "1+e"; # False
s10 = " "; # False
s11 = "e9"; # False
s12 = "4e+"; # False
s13 = " -."; # False
s14 = "+.8"; # True
s15 = " 005047e+6"; # True
s16 = ".e1"; # False
s17 = "3.e"; # False
s18 = "3.e1"; # True
s19 = "+1.e+5"; # True
s20 = " -54.53061"; # True
s21 = ". 1"; # False

print(Solution().isNumber(s21))
        
# @lc code=end

