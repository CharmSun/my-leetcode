#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while i > -1:
            s = digits[i] + carry
            digits[i] = s % 10
            carry = s // 10
            i -= 1
            if carry == 0:
                break
        if carry != 0:
            return [carry] + digits
        return digits

input = [4,3,2,1]  
print(Solution().plusOne(input))
        
# @lc code=end

