#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start

# 厄拉多塞筛法，思想是假如当前数是i,那么范围n内所有i的倍数肯定不是质数，用一个bool数组记录下来。
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        flags = [False] * n
        count = 0
        for i in range(2, n):
            if flags[i] == False:
                count += 1
            for j in range(2*i, n, i):
                flags[j] = True
        return count
        
# @lc code=end

