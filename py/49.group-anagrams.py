#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
from typing import List

## 将字符串按字母排序后作为key 存hash， value为结果数组中的位置
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_map = {}
        result = []
        for s in strs:
            tmp = ''.join(sorted(s))
            if tmp not in str_map:
                str_map[tmp] = len(result)
                result.append([s])
            else:
                result[str_map[tmp]].append(s)
        return result

input = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(input))

# @lc code=end

