#
# @lc app=leetcode id=150 lang=python3
#
# [150] Evaluate Reverse Polish Notation
#

# @lc code=start
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oper = ['+', '-', '*', '/']
        for char in tokens:
            if char not in oper:
                stack.append(int(char))
            else:
                top1 = stack.pop()
                top2 = stack.pop()
                if char == '+':
                    stack.append(top2 + top1)
                elif char == '-':
                    stack.append(top2 - top1)
                elif char == '*':
                    stack.append(top2 * top1)
                elif char == '/':
                    stack.append(int(top2 / top1))
        return stack.pop()

input = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(Solution().evalRPN(input))
        
# @lc code=end

