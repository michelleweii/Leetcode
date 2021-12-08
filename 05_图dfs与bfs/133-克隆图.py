"""
middle 2021-12-09

"""
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node):
        collect={}
        def search(node):
            if not node:
                return
            newnode=Node(node.val,[])
            collect[node]=newnode
            for i in node.neighbors:
                if i not in collect:
                    newnode.neighbors.append(search(i))
                else:
                    newnode.neighbors.append(collect[i])
            return newnode
        return search(node)

if __name__ == '__main__':
    # adjList = [[2,4],[1,3],[2,4],[1,3]]
    # print(Solution().cloneGraph(adjList))