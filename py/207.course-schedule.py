#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        for e in prerequisites:
            indegree[e[0]] += 1
        queue = []
        for v in range(numCourses):
            if indegree[v] == 0:
                queue.append(v)
        count = 0
        while queue:
            v = queue.pop(0)
            count += 1
            for e in prerequisites:
                if e[1] == v:
                    indegree[e[0]] -= 1
                    if indegree[e[0]] == 0:
                        queue.append(e[0])
        return count == numCourses

numCourses = 3
prerequisites = [[1,0],[2,1]]        
print(Solution().canFinish(numCourses, prerequisites))
# @lc code=end

