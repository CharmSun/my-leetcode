#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start

## KMP算法
## 1、思想：失配时尽量移动模式串needle，i不变，移动j
## 2、next [j] = k，代表j 之前的字符串中有最大长度为k 的相同前缀后缀。next[j]的值（也就是k）表示，当haystack[j] != needle[i]时，j指针的下一步移动位置。
## 3、求next, needle[n] == needle[k]时，则next[n + 1 ] = next [n] + 1 = k + 1
## 4、needle[n] != needle[k]时，递归 k=next[k]
## 5、needle[j] != haystack[i]时，移动j 为 next[j]
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        next = [-1] * len(needle)
        k = -1
        n = 0
        ## needle[k]表示前缀，needle[n]表示后缀    
        while n < len(needle) - 1:
            if k == -1 or needle[n] == needle[k]:
                n += 1
                k += 1
                if needle[n] != needle[k]:
                    next[n] = k
                else: 
                    next[n] = next[k]  ## 对next数组进一步的优化，当相同时，跳过无意义的比较
            else:
                k = next[k]
        i = 0
        j = 0
        while i < len(haystack) and j < len(needle):
            if j == -1 or needle[j] == haystack[i]: ## 当j为-1时，要移动的是i，当然j也要归0
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(needle):
            return i - j
        else:
            return -1
        
# @lc code=end

