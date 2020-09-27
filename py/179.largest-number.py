#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#

# @lc code=start
from typing import List
from functools import cmp_to_key

## 排序时自定义比较函数，'3' + '30' > '30' + '3'
## 返回结果注意都是 0 的情形
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a,b):
            str1 = str(a)+str(b)
            str2 = str(b)+str(a)
            if str1 > str2:
                return -1
            elif str1 < str2:
                return 1
            else:
                return 0
        strs = [str(i) for i in nums]
        strs.sort(key = cmp_to_key(cmp))
        print(strs)
        return '0' if strs[0] == '0' else ''.join(strs)

input = [3,30,34,5,9]
print(Solution().largestNumber(input))
        
# @lc code=end

