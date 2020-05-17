#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start

## 栈的经典使用，处理每个path，'.'继续，'..'退栈，其他入栈
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = [p for p in path.split('/') if p]
        for p in path:
            if p == '.':
                continue
            elif p == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return '/'+ '/'.join(stack)

input = "/a//b////c/d//././/.."
print(Solution().simplifyPath(input))
        
# @lc code=end

