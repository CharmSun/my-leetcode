#
# @lc app=leetcode id=131 lang=python3
#
# [131] Palindrome Partitioning
#

# @lc code=start
from typing import List

## dfs, 拆分判断回文
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        result = []
        self.dfs(s, [], result)
        return result

    def isPalindrome(self, s) -> bool:
        i = 0
        j = len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def dfs(self, s, ans, result):
        if not s:
            result.append(ans)
            return None
        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.isPalindrome(prefix):
                self.dfs(s[i:], ans+[prefix], result)

input = 'aab'
print(Solution().partition(input))
        
# @lc code=end

