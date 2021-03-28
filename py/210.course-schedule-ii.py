#
# @lc app=leetcode id=210 lang=python3
#
# [210] Course Schedule II
#

# @lc code=start
from typing import List

class Solution:
    # 拓扑算法
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indgree = [0] * numCourses
        for e in prerequisites:
            indgree[e[0]] += 1
        queue = []
        for v in range(numCourses):
            if indgree[v] == 0:
                queue.append(v)
        count = 0
        res = []
        while queue:
            v = queue.pop(0)
            count += 1
            res.append(v)
            for e in prerequisites:
                if e[1] == v:
                    indgree[e[0]] -= 1
                    if indgree[e[0]] == 0:
                        queue.append(e[0])
        if count != numCourses:
            return []
        return res
        
# @lc code=end

