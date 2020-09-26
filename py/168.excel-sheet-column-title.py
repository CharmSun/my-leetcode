#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start

## ord 将字符转为AscII码，chr 将AscII 码转为字符
class Solution:
    def convertToTitle(self, n: int) -> str:
        if n <= 0:
            return ''
        chars = []
        for i in range(26):
            chars.append(chr(ord('A') + i))
        a = n - 1
        res = ''
        while a >= 0:
            b = a % 26
            res = chars[b] + res
            a = a // 26 - 1
        return res

print(Solution().convertToTitle(701))  
        
# @lc code=end

