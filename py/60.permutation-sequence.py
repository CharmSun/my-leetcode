#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start

## f[i] 表示i个数有多少个组合结果
## j 表示应该取 num_str 中第几个数，取完后，从num_str中去掉
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num_str = '123456789'
        f = [1] * n
        for i in range(1, n):
            f[i] = f[i - 1] * i
        res = ''
        k -= 1
        for i in range(0, n):
            j = k // f[n - 1 - i]
            k = k % f[n - 1 - i]
            res += num_str[j]
            num_str = num_str[0:j] + num_str[j+1:]
        return res

print(Solution().getPermutation(3, 3))
        
# @lc code=end

