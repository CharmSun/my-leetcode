#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List

## 折半查找：
## 1、判断num1， nums2长短，m取短的数组，n取长的数组
## 2、i 在[0,m]中折半查找，分情况增大或缩小，确定左边部分，和右边部分，计算中位值
## 3、m+n为奇数时，为max(nums1[i-1], nums2[j-1])；为偶数时，为（max(nums1[i-1], nums2[j-1]) + min(nums1[i], nums2[j])）/ 2

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            temp = nums2
            nums2 = nums1
            nums1 = temp
            m,n = n,m
        iMin, iMax, halfLen = 0, m, (m + n + 1) // 2
        while iMin <= iMax:
            i = (iMin + iMax) // 2
            j = halfLen - i
            # 增大i
            if i < m and nums2[j-1] > nums1[i]:
                iMin = i + 1
            # 缩小i
            elif i > 0 and nums1[i-1] > nums2[j]:
                iMax = i - 1
            else:
                maxLeft = minRight = 0
                if i == 0:
                    maxLeft = nums2[j-1]
                elif j == 0:
                    maxLeft = nums1[i-1]
                else:
                    maxLeft = max(nums1[i-1], nums2[j-1])
                    
                if (m + n) % 2 == 1:
                    return maxLeft
                
                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else: 
                    minRight = min(nums1[i], nums2[j])
                    
                return (maxLeft + minRight) / 2
        
# @lc code=end

