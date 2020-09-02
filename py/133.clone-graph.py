#
# @lc app=leetcode id=133 lang=python3
#
# [133] Clone Graph
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    ## BFS
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        queue = [node]
        root = Node(node.val)
        visited = dict()
        visited[node.val] = root
        while queue:
            top = queue.pop(0)
            for n in top.neighbors:
                if n.val in visited:
                    visited[top.val].neighbors.append(visited[n.val])
                else:
                    new_node = Node(n.val)
                    visited[top.val].neighbors.append(new_node)
                    visited[n.val] = new_node
                    queue.append(n)
        return root
    
    ## DFS
    def cloneGraph1(self, node: 'Node') -> 'Node':
        if not node:
            return None
        root = Node(node.val)
        visited = dict()
        visited[node.val] = root
        self.dfs(node, visited)
        return root

    def dfs(self, node, visited):
        for i in node.neighbors:
            if i.val in visited:
                visited[node.val].neighbors.append(visited[i.val])
            else:
                new_node = Node(i.val)
                visited[node.val].neighbors.append(new_node)
                visited[i.val] = new_node
                self.dfs(i, visited)
        
# @lc code=end

