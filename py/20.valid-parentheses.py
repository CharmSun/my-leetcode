#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start

## 栈的基础使用
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in map:
                stack.append(char)
            if char in map.values() :
                if len(stack) > 0 and char == map[stack[-1]]:
                    stack.pop()
                else:
                    return False
        return not stack

print(Solution().isValid("]"))

# @lc code=end

