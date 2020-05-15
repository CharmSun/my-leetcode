#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curLineWords = []  ## 存放当前行的单词
        wordsLen = 0  ## 当前行单词的总长度
        res = []
        for w in words:
            ## 加一个单词就超过了
            if wordsLen + len(curLineWords) + len(w) > maxWidth:
                if curLineWords:
                    for i in range(maxWidth - wordsLen):
                        idx = len(curLineWords) - 1 if len(curLineWords) > 1 else 1
                        curLineWords[i % idx] += ' '  ## 平均分配下空格
                    res.append(''.join(curLineWords))
                    curLineWords = []
                    wordsLen = 0
            if wordsLen + len(curLineWords) + len(w) <= maxWidth:
                curLineWords.append(w)
                wordsLen += len(w)
        if curLineWords:  ## 处理最后一行
            last = ' '.join(curLineWords)
            for i in range(len(last), maxWidth):
                last += ' '
            res.append(last)
        return res

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
print(Solution().fullJustify(words, maxWidth))  
        
# @lc code=end

