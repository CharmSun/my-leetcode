#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
from typing import List
from collections import deque

# @lc code=start
class Solution:
    # 双端队列，存放有可能成为滑动窗口最大值数值的下标。
    # 队头为滑动窗口最大值的下标
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if not nums or k < 1 or k > len(nums):
            return res
        window = deque([])
        for i,num in enumerate(nums):
            if window and i - window[0] >= k:
                window.popleft()
            while window and nums[window[-1]] <= num:
                window.pop()
            window.append(i)
            if i >= k - 1:
                res.append(nums[window[0]])
        return res

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(Solution().maxSlidingWindow(nums, k))
        
# @lc code=end

