#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start

## manacher算法：
## 1、加入间隔分隔符'#', 构造奇数长度的字符串
## 2、i < mr 时，r[i] = min(r[2*id - i], mr - i)
## 3、继续匹配，按情况更新延伸至最右端回文串，及其中心，记录最长的回文串及其中心位置
## 4、计算原始回文串

class Solution:
    def longestPalindrome(self, s: str) -> str:
        newStr = '#'
        for i in range(len(s)):
            newStr += s[i]
            newStr += '#'
        mr = 0 # 已找到回文串延伸到的最右端的位置
        id = 0 # 该回文串的中心
        maxRadius = 0 # 新串中最大回文子串半径
        maxCenter = 0 # 新串中最大回文子串中心
        r = [0 for i in range(len(newStr))]
        for i in range(len(newStr)):
            r[i] = min(r[2*id - i], mr-i) if i < mr else 1
            while i - r[i] >= 0 and i+r[i] <= len(newStr) - 1 and newStr[i + r[i]] == newStr[i - r[i]]:
                r[i] += 1
            if mr < i + r[i]:
                mr = i + r[i]
                id = i
            if maxRadius < r[i]:
                maxRadius = r[i]
                maxCenter = i
        start = (maxCenter + 1 - maxRadius) // 2
        mlen = maxRadius - 1
        return s[start: start + mlen]
        
# @lc code=end

