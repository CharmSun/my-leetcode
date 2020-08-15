#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#

# @lc code=start
class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)

        commonX = 0
        commonY = 0
        if G > A and C > E:
            commonX = min(C, G) - max(A, E)
        if H > B and D > F:
            commonY = min(D, H) - max(B, F)
        
        return area1 + area2 - commonX * commonY

A, B , C , D, E,F,G,H = -2,-2,2,2,-3,-3,3,-1
print(Solution().computeArea(A,B,C,D,E,F,G,H))

        
# @lc code=end

