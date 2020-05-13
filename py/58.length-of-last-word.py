#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#

# @lc code=start

## 倒着数
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        count = 0
        startCount = False
        while i >= 0:
            if s[i] == ' ' and startCount:
                break
            if s[i] != ' ':
                count += 1
                if not startCount:
                    startCount = True
            i -= 1
        return count

input = "Hello World"
print(Solution().lengthOfLastWord(input))
        
# @lc code=end

