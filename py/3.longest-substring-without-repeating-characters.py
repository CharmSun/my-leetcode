#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start

## 滑动窗口记录 不含重复字符的子串，left指向左边界
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        ans = left = 0
        dict = {}
        for i in range(length):
            if s[i] in dict:
                left = max(dict[s[i]], left)
            if i-left+1 > ans:
                ans = i-left+1
            dict[s[i]] = i + 1 
        return ans
        
# @lc code=end

