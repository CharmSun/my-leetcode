#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        str_map1, str_map2 = {}, {}
        s_len, t_len = len(s), len(t)
        if s_len != t_len:
            return False
        for i in range(s_len):
            if str_map1.get(s[i]) != str_map2.get(t[i]):
                return False
            str_map1[s[i]] = str_map2[t[i]] = i
        return True
        
# @lc code=end

