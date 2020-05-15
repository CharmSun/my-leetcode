#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start

## 二分查找
class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        up = x
        while low <= up:
            mid = (low + up) // 2
            s = mid * mid
            if s == x:
                return mid
            elif s < x:
                low = mid + 1
            else:
                up = mid - 1
        return up

print(Solution().mySqrt(8))
        
# @lc code=end

