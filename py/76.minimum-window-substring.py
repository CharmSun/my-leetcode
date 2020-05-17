#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start

## 双指针滑动窗口：
## 1、串t存储到hash
## 2、right移动，遇到有效符合串s的（多余的字符不算），count += 1
## 3、count 等于串t的长度时，计算最小长度，判断left在hash字典中，减少count, 不停收缩left
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''
        res = ''
        m = {}
        for char in t:
            if char in m:
                m[char] += 1
            else:
                m[char] = 1
        left = right = 0
        count = 0
        minLen = len(s) + 1
        while right < len(s):
            if s[right] in m:
                m[s[right]] -= 1
                if m[s[right]] >= 0:
                    count += 1
                while count == len(t):
                    if right - left + 1 < minLen:
                        res = s[left:right+1]
                        minLen = right - left + 1
                    if s[left] in m:
                        m[s[left]] += 1
                        if m[s[left]] > 0: 
                            count -= 1
                    left += 1
            right += 1
        return res

S = "aedbbac"
T = "abc"
print(Solution().minWindow(S, T)) 
        
# @lc code=end

