#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#

# @lc code=start
import collections
from typing import List

class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True

    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord  

class Solution:
    ## 构建字典树，dfs查找
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        trie = Trie()
        node = trie.root
        for word in words:
            trie.insert(word)
        # visited = [[False for j in range(len(board[0]))] for i in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, node, i, j, "", res)
        return res
    
    def dfs(self, board, node ,i, j, path, res):
        if node.isWord:
            res.append(path)
            node.isWord = False
        if i < 0 or i>= len(board) or j < 0 or j >= len(board[0]):
            return
        # if visited[i][j]:
        #     return
        cur = board[i][j]
        node = node.children.get(cur)
        if not node:
            return
        board[i][j] = "#"
        self.dfs(board, node, i+1, j, path+cur, res)
        self.dfs(board, node, i-1, j, path+cur, res)
        self.dfs(board, node, i, j+1, path+cur, res)
        self.dfs(board, node, i, j-1, path+cur, res)
        board[i][j] = cur
        
# @lc code=end

