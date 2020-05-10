#
# @lc app=leetcode id=38 lang=python3
#
# [38] Count and Say
#

# @lc code=start

## 一项一项递推
class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        for i in range(1, n):
            count = 0
            numChar = res[0]
            cur = ''
            for c in res:
                if c == numChar:
                    count += 1
                else:
                    cur += str(count) + numChar
                    numChar = c
                    count = 1
            cur += str(count) + numChar
            res = cur
        return res

print(Solution().countAndSay(5))
        
# @lc code=end

