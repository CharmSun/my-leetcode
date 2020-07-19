#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(i) for i in version1.split('.')]
        v2 = [int(i) for i in version2.split('.')]

        l1, l2 = len(v1), len(v2)
        max_len = max(l1, l2)

        v1 += [0] * (max_len - l1)
        v2 += [0] * (max_len - l2)

        for a,b in zip(v1, v2):
            if a > b:
                return 1
            elif a < b:
                return -1
        
        return 0

version1 = "7.5.2.4"
version2 = "7.5.3"
print(Solution().compareVersion(version1, version2))

# @lc code=end

