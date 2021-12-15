"""
middle 2021-12-16
https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/fu-xue-ming-zhu-dan-diao-zhan-die-dai-la-dkrm/
https://leetcode-cn.com/problems/binary-search-tree-iterator/solution/xiang-jie-ru-he-dui-die-dai-ban-de-zhong-4rxj/
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: TreeNode):
        pass


    def next(self) -> int:
        pass


    def hasNext(self) -> bool:
        pass

if __name__ == '__main__':
    a = TreeNode(7)
    b = TreeNode(3)
    c = TreeNode(15)
    d = TreeNode(9)
    e = TreeNode(20)
    a.right = c
    a.left = b
    c.right = e
    c.left = d
    obj = BSTIterator(a)
    param_1 = obj.next()
    param_2 = obj.hasNext()