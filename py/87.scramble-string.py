#
# @lc app=leetcode id=87 lang=python3
#
# [87] Scramble String
#

# @lc code=start

## 1、先判断简单边界情况
## 2、递归，s1和s2是scramble的话，那么必然存在一个在s1上的长度l1，将s1分成s11和s12两段
## 同样有s21和s22.那么要么s11和s21是scramble的并且s12和s22是scramble的；
## 要么s11和s22是scramble的并且s12和s21是scramble的
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        l1, l2 = list(s1), list(s2)
        l1.sort()
        l2.sort()
        str1 = ''.join(l1)
        str2 = ''.join(l2)
        if str1 != str2:
            return False
        for i in range(1, len(s1)):
            s1left = s1[0:i]
            s1right = s1[i:]
            s2left = s2[0:i]
            s2right = s2[i:]
            if self.isScramble(s1left, s2left) and self.isScramble(s1right, s2right):
                return True
            s2left = s2[0:len(s1) - i]
            s2right = s2[len(s1) - i:]
            if self.isScramble(s1left, s2right) and self.isScramble(s1right, s2left):
                return True
        return False
        
# @lc code=end

