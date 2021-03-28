#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start

## 利用hash表，对每个字母一个加1，一个减1，最后hash表中所有字母值为0
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic = {}
        for i in range(len(s)):
            c1 = dic.get(s[i], 0) + 1
            dic[s[i]] = c1
            c2 = dic.get(t[i], 0) - 1
            dic[t[i]] = c2
        for key in dic:
            if dic[key] != 0:
                return False
        return True
        
# @lc code=end

