#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        if n <= 0:
            return res
        def backtrack(s, lnum, rnum):
            if lnum == n and rnum == n:
                res.append(s)
            if lnum < n:
                backtrack(s + '(', lnum+1, rnum)
            if lnum > rnum and rnum < n:
                backtrack(s + ')', lnum, rnum+1)
        
        backtrack('', 0, 0)
        return res

print(Solution().generateParenthesis(3))
        
# @lc code=end

