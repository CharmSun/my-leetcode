#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
from typing import List

INT_MIN = - 2 ** 31
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.divide(nums, 0, len(nums) - 1)
    
    # 方法1：动态规划，dp[i]以第i个元素为结尾的一段最大子序和，演变一下只用变量sum
    def dp(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max = sum = nums[0]
        for i in range(1, len(nums)):
            if sum <= 0:
                sum = nums[i]
            else:
                sum += nums[i]
            if sum > max:
                max = sum
        return max
    
    # 方法2：分治
    ## 1、求左半部分连续最大和，求右半部分连续最大和
    ## 2、求经过中间值的连续值的最大和
    ## 3、取三者的最大者，即为结果
    def divide(self, nums, left, right):
        if not nums:
            return 0
        if left == right:
            return nums[left]
        if left > right:
            return INT_MIN
        mid = (left + right) // 2
        leftSum = self.divide(nums, left, mid - 1)
        rightSum = self.divide(nums, mid + 1, right)

        maxMidLeft = 0
        maxMidRight = 0
        sumL = sumR = 0
        for i in range(mid - 1, left - 1, -1):
            sumL += nums[i]
            maxMidLeft = max(maxMidLeft, sumL)
        for i in range(mid + 1, right + 1, 1):
            sumR += nums[i]
            maxMidRight = max(maxMidRight, sumR)
        return max(leftSum, rightSum, maxMidLeft + nums[mid] + maxMidRight)
        
# @lc code=end

