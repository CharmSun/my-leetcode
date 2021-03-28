#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#

# @lc code=start
from typing import List

## 递归
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i in range(1, len(expression)):
            if expression[i] in '+-*':
                left = self.diffWaysToCompute(expression[0:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        res.append(self.calc(expression[i], l, r))
        return res
    
    def calc(self, op, a, b):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        else:
            raise Exception('wrong operation')

input = "2*3-4*5"
print(Solution().diffWaysToCompute(input))
        
# @lc code=end

