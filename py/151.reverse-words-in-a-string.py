#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1]) # 剔除所有空格字符返回数组并反转，以空格为间隔把数组拼成字符串
        
# @lc code=end

