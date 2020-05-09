#
# @lc app=leetcode id=30 lang=python3
#
# [30] Substring with Concatenation of All Words
#

# @lc code=start
from typing import List 

## 1、先用一个哈希表 wordsDict 来记录words里的所有词，
## 2、然后我们从0开始遍历，用left来记录左边界的位置，count表示当前已经匹配的单词的个数。
## 3、如果当前遍历的到的单词在 wordsDict 中存在，那么我们将其加入另一个哈希表 curMap 中，
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not s or not words:
            return res
        strLen = len(s)
        wordLen = len(words[0])
        if strLen < wordLen * len(words):
            return res
        wordsDict = {}
        for word in words:
            wordsDict[word] = wordsDict.get(word, 0) + 1
        for i in range(wordLen):
            curMap = {}
            count = 0
            left = i
            for j in range(i, strLen - wordLen + 1, wordLen):
                curWord = s[j:j+wordLen]
                if curWord in wordsDict:
                    curMap[curWord] = curMap.get(curWord, 0) + 1
                    if curMap[curWord] <= wordsDict[curWord]:
                        count += 1
                    else:
                        while curMap[curWord] > wordsDict[curWord]:
                            tmp = s[left:left+wordLen]
                            curMap[tmp] -= 1
                            if tmp != curWord:
                                count -= 1
                            left += wordLen
                    if count == len(words):
                        res.append(left)
                        tmp = s[left:left+wordLen]
                        curMap[tmp] -= 1
                        count -= 1
                        left += wordLen
                else:
                    curMap.clear()
                    count = 0
                    left = j + wordLen
        return res

s = "barfoofoobarthefoobarman"
words = ["bar","foo","the"]
print(Solution().findSubstring(s, words))
        
# @lc code=end

