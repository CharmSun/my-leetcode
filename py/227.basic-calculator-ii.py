#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    ## 栈的使用
    def cal(self, num1, num2, op):
        if op == '+':
            return num1 + num2
        elif op == '-':
            return num1 - num2
        elif op == '*':
            return num1 * num2
        elif op == '/':
            return num1 // num2

    def calculate(self, s: str) -> int:
        opPriority = {'+': 1, '-': 1, '*': 2, '/': 2}
        numStack = []
        opStack = []
        i = 0
        while i < len(s):
            if s[i] >= '0' and s[i] <= '9':
                start = i
                while i < len(s) and s[i] >= '0' and s[i] <= '9':
                    i += 1
                num = int(s[start:i])
                numStack.append(num)
            elif s[i] in opPriority:
                if not opStack:
                    opStack.append(s[i])
                else:
                    opTop = opStack[len(opStack) - 1]
                    while opPriority[opTop] >= opPriority[s[i]]:
                        num2 = numStack.pop()
                        num1 = numStack.pop()
                        calRes = self.cal(num1, num2, opTop)
                        numStack.append(calRes)
                        opStack.pop()
                        if not opStack:
                            break
                        else:
                            opTop = opStack[len(opStack) - 1]
                    opStack.append(s[i])
                i += 1
            else:
                i += 1

        while opStack:
            opTop = opStack.pop()
            num2 = numStack.pop()
            num1 = numStack.pop()
            calRes = self.cal(num1, num2, opTop)
            numStack.append(calRes)

        return numStack.pop()

print(Solution().calculate(' 3/2 ')) 
        
# @lc code=end

