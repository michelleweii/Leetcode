二叉树的最大深度：<u>根节点的高度</u>就是二叉树的最大深度。（从上向下计算）

二叉树节点的高度：指从该节点到叶子节点的最长简单路径<u>节点数量</u>。（从下向上计算）

二叉树的最小深度：最小深度是从根节点到最近叶子节点的最短路径上的<u>节点数量</u>。

[关于二叉树的高度与深度图解](https://www.programmercarl.com/0110.%E5%B9%B3%E8%A1%A1%E4%BA%8C%E5%8F%89%E6%A0%91.html#%E9%80%92%E5%BD%92)

# 二叉树遍历

- [二叉树的四种遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/solution/tu-jie-er-cha-shu-de-si-chong-bian-li-by-z1m/)

> 递归三部曲
>
> 1. 确定递归函数的参数和返回值
> 2. 确定终止条件
> 3. 确定单层递归的逻辑

## 前序遍历（递归）

```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if not root: return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)
```

## 前序遍历（迭代）

```python
# 前序遍历
# 和中序一样，都是先到达最左端叶子节点
def preorderTraversal(root):
    if not root:return []
    cur, stack, res = root, [], []
    while cur or stack:
        while cur: # 根节点和左孩子入栈
            res.append(cur.val) # 前序与中序不同点
            stack.append(cur)
            cur = cur.left
        tmp = stack.pop() # 每弹出一个元素，就到达右孩子
        cur = tmp.right
    return res
```

## 中序遍历（递归）

```python
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.helper(root,res) # 递归调用中序遍历
        return res
    def helper(self,root,res):
        if not root:return 
        self.helper(root.left, res) # 左
        res.append(root.val) # 根
        self.helper(root.right, res) # 右
```

## 中序遍历（迭代）

```python
# 中序迭代-栈
# 和前序遍历的代码完全相同，只是在出栈的时候才将节点 tmp 的值加入到结果中。
def inorderTraversal(root):
    if not root: return []
    stack, res, cur = [], [], root
    while stack or cur:
        while cur:  # cur入栈，并到达最左端的叶子节点
            stack.append(cur)
            cur = cur.left  # 左子树不断入栈
        tmp = stack.pop()
        res.append(tmp.val)  # 出栈时再加入结果
        cur = tmp.right  # 遍历右节点，再将右节点的左子树全部入栈
    return res
```

## 后序遍历（递归）

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if not root: return
        self.helper(root.left, res)
        self.helper(root.right, res)
        res.append(root.val)
```

## 后序遍历（迭代）

```python
# 类比前序遍历的常规解法，我们只需要将输出的“根 -> 左 -> 右”的顺序改为“左 -> 右 -> 根”就可以了。
# 如何实现呢？这里有一个小技巧，我们入栈时额外加入一个标识，比如这里使用 flag = 0；
# 然后每次从栈中弹出元素时，如果 flag 为 0，则需要将 flag 变为 1 并连同该节点再次入栈，只有当 flag 为 1 时才可将该节点加入到结果中。
def post_travel(root):
    if not root:return []
    stack, res = [(0,root)], []
    while stack:
        flag, node = stack.pop()
        if not node:continue
        if flag==1:
            res.append(node.val)
        else:
            stack.append((1, node))
            stack.append((0, node.right)) # 右
            stack.append((0, node.left)) # 左
    return res
```

## 迭代模板

```python
边界条件

初始化cur,stack,root
while stack 或 cur 非空:
  	while 循环：
  		cur向左下或右下遍历
    	cur的值入栈
 		弹出节点tmp
    cur回到tmp的左或右子树
返回结果
```

## 层次遍历

> 层次遍历是BFS（广度优先遍历）

```python
def LevelOrder(root):
    res = []
    if not root:return res    
    queue = [root]
    # flag = 1 # zigzag
    while queue:
        # 记录当前层的所有节点，当前层的数量（扩展其孩子）
        cur_level, cur_size = [], len(queue)
        # 当前层开始循环
        for i in range(cur_size):
            cur = queue.pop(0) # 队首元素出队
            cur_level.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
        res.append(cur_level[:])
        # res.append(cur_level[::flag]) # # zigzag
        # flag *= -1 # zigzag
    return res
```

应用：

102.二叉树的层序遍历；103.二叉树zigzag遍历；104.二叉树的最大深度；

199.二叉树的右视图；429.N叉树的前序遍历；515.在每个树行中找最大值；637.二叉树的层平均值

## morris遍历

二叉树遍历算法的超强进阶算法，morris遍历可以将非递归遍历中的空间复杂度降为O(1)。

# 树回溯

LC257.二叉树的所有路径，树回溯的基础的基础的基础！

**递归函数的return：对递归函数什么时候要有返回值，什么时候不能有返回值很迷茫?**
**如果需要遍历整颗树，递归函数就不能有返回值。如果需要遍历某一条固定路线，递归函数就一定要有返回值！**

递归函数什么时候需要返回值？什么时候不需要返回值？这里总结如下三点：

- 如果需要搜索整颗二叉树且不用处理递归返回值，递归函数就不要返回值。（这种情况就是本文下半部分介绍的113.路径总和ii）
- 如果需要搜索整颗二叉树且需要处理递归返回值，递归函数就需要返回值。 （这种情况我们在[236. 二叉树的最近公共祖先 (opens new window)](https://programmercarl.com/0236.二叉树的最近公共祖先.html)中介绍）
- 如果要搜索其中一条符合条件的路径，那么递归一定需要返回值，因为遇到符合条件的路径了就要及时返回。（lc112.路径总和）**因为搜索到目标节点了，就要立即return了，这样才是找到节点就返回（搜索某一条边），如果不加return，就是遍历整棵树了。(具体可看LC700)**

```python
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。
# 从根节点到叶子的路径，所以需要前序遍历。
# 1、递归出口：到达叶子节点；
# 2、回溯，回溯和递归是一一对应的，有一个递归，就要有一个回溯。
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []
        self.path = []

    def binaryTreePaths(self, root: TreeNode):# -> List[str]:
        if not root:return self.res
        self.backtrace(root)
        return self.res

    def backtrace(self, cur):
        self.path.append(str(cur.val)) # 先添加

        # 递归出口：到达叶子节点
        if cur.left is None and cur.right is None:
            self.res.append('->'.join(self.path))

        if cur.left:
            self.backtrace(cur.left)
            self.path.pop() # 回溯和递归是一一对应的，有一个递归，就要有一个回溯。

        if cur.right:
            self.backtrace(cur.right)
            self.path.pop() # 回溯和递归是一一对应的，有一个递归，就要有一个回溯。
```



> 相关题目
>
> LC112->LC113-> 
>
> LC513



# 构造树

构造树一般采用的是前序遍历，因为先构造中间节点，然后递归构造左子树和右子树。



# 二叉搜索树BST

> 性质：对于树中每个节点,若其左子树存在，则其左子树中每个节点的值都不大于该节点值；若其右子树存在，则其右子树中每个节点的值都不小于该节点值。
>
> BST的中序遍历是升序的。等同于根据中序遍历的序列恢复BST。



应用：





# 平衡二叉树AVL

> 性质：左右子树高度差不超过1。

```python
# 判断树是否是平衡二叉树
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
            self.isBalanced(root.left) and self.isBalanced(root.right)
		# 求树高度
    def depth(self, root):
        if not root: return 0
        return max(self.depth(root.left), self.depth(root.right)) + 1
```

