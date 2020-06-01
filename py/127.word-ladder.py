#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#

# @lc code=start
from typing import List
from collections import deque, defaultdict

## 广度优先算法:
## 将每一层上可以生成的单词全部列出来，然后再逐层遍历，
# 一旦出现一个单词等于endWord，那么遍历终止，将当前遍历的次数返回
## 要注意的是，需要将已经遍历的单词记录下来，从而不会发生重复的情况。
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queue for BFS
        queue = deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()      
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []
        return 0

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(Solution().ladderLength(beginWord, endWord, wordList))


        
# @lc code=end

