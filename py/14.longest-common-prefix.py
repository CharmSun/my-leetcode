#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ''
        if not strs:
            return pre
        i = 0
        while True:
            c = ''
            for word in strs:
                if i >= len(word):
                    return pre
                if not c:
                    c = word[i]
                if word[i] != c:
                    return pre
            pre += c
            i += 1
        
# @lc code=end

