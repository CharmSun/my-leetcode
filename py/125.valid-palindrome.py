#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start

## 双指针指向头尾，开始比较
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j:
                if s[i].lower() != s[j].lower():
                    return False
                else:
                    i += 1
                    j -= 1
        return True

print(Solution().isPalindrome(".,"))

# @lc code=end

