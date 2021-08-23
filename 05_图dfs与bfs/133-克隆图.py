
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
    pass