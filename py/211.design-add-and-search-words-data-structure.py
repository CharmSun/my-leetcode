#
# @lc app=leetcode id=211 lang=python3
#
# [211] Design Add and Search Words Data Structure
#

# @lc code=start
import collections

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
        

    def search(self, word: str) -> bool:
        node = self.root
        return self.dfs(node, word)
    
    def dfs(self, node: TrieNode, word: str) -> bool:
        if not word:
            return node.isWord
        if word[0] == '.':
            for k in node.children:
                if self.dfs(node.children[k], word[1:]):
                    return True
        else:
            n = node.children.get(word[0])
            if not n:
                return False
            return self.dfs(n, word[1:])
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

