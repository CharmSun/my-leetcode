#
# @lc app=leetcode id=190 lang=python3
#
# [190] Reverse Bits
#

# @lc code=start
## 将长度32的 无符号int 拆解成4个长度为8 的byte. 每8个byte对应的值
## 可以作为片段存在缓存中，只要遇到重复的片段，就可以直接返回。
class Solution:
    def __init__(self) -> None:
        self.cache = {}

    def reverseByte(self, byte):
        if byte in self.cache:
            return self.cache[byte]
        val = 0
        for i in range(8):
            val += ((byte>>i) & 1)
            # byte >>=1
            if i < 7:
                val <<=1
        self.cache[byte] = val
        return val
        
        
    def reverseBits(self, n: int) -> int:
        res = 0
		#reverse each byte and append it to the result
        for i in range(4):
            byte = (n >> 8*i) & 0xFF
            res |= self.reverseByte(byte)
            if i < 3:
                res <<=8
        return res
        
# @lc code=end

