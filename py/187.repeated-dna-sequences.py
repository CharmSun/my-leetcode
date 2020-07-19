#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#

# @lc code=start
from typing import List

## 将10位字符序列看成二进制，换算成十进制，作为hash_map的key, 节省空间
## 只有ACGT四种字符，看成 00， 01，10， 11
## seq_set 用set 保存已有的字符序列代表的hash值
## 结果res也用set记录，放置结果重复

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []
        res = set()
        seq_set = set()
        map = { 'A': 0, 'C': 1, 'G': 2, 'T': 3 }
        v = 0
        for i in range(len(s)):
            v = ( v << 2 | map[s[i]]) & 0xfffff
            if i < 9:
                continue
            elif v in seq_set:
                res.add(s[i-9:i+1])
            else:
                seq_set.add(v)
        return list(res)

s = "AAAAAAAAAAAA"
print(Solution().findRepeatedDnaSequences(s))        
# @lc code=end

