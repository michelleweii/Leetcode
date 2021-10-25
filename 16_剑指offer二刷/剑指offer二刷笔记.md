剑指offer二刷笔记 

遗留的问题 **https://github.com/michelleweii/Leetcode**

- [ ] 14-1 剪绳子 middle
- [ ] 14-2 剪绳子2 middle
- [ ] 43 1～n 整数中 1 出现的次数 hard
- [ ] 44 数字序列中某一位的数字 middle 找规律
- [ ] 56-2 数组中数字出现的次数 II middle
- [ ] 60 n个骰子的点数 hard dp
- [ ] 62 圆圈中最后剩下的数字 easy 约瑟夫环
- [ ] 65 不用加减乘除做加法 easy 位运算

# 1. 目录

## 1【哈希表】

#### 03 数组中重复的数字

```python
def findRepeatNumber(self, nums):
    n = len(nums)
    for i in range(n):
        while nums[i] != i:
            if nums[nums[i]] == nums[i]: return nums[i]
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
    return -1
```

#### 39 数组中出现次数超过一半的数字

```python
def majorityElement(self, nums):
    if not nums:return nums
    n = len(nums)
    half = n//2
    hash_map = {}
    for x in nums:
        hash_map[x] = hash_map.get(x,0)+1
        if hash_map.get(x,0)>half:
            return x
# 摩尔投票法
def majorityElement1(self, nums):
    cnt = 0
    val = -1
    for x in nums:
        if not cnt:
            val=x
            cnt+=1
        else:
            if x==val:cnt+=1
            else:cnt-=1
    return val
```

#### 50 第一个只出现一次的字符

```python
def firstUniqChar(self, s: str):
    hashmap = {}
    for x in s:
        hashmap[x] = True if x not in hashmap else False
    for x in s:
        if hashmap[x]:return x
    return " "
```

#### 57-1 和为s的两个数字

```python
def twoSum(self, nums, target):
    if not nums:return []
    hashmap = {}
    for x in nums:
        # print(hashmap)
        if hashmap.get(x,0):return [x, hashmap[x]]
        hashmap[target-x] = x
    return []
```



## 2【双指针】

#### 21 调整数组顺序使奇数在前（反向双指针）

```python
def exchange(self, nums):
    n = len(nums)
    i, j = 0, n-1
    while i<j:
        if i<n and nums[i]%2==1: i+=1
        if j>=0 and nums[j]%2==0: j-=1
        else: nums[i], nums[j] = nums[j], nums[i]
    return nums
```

#### **48 *最长不含重复字符的子字符串（同向双指针）**middle

```python
def lengthOfLongestSubstring(self, s):
    if not s: return 0
    hashmap = {}
    i = 0
    res = -1
    for j in range(len(s)):
        # if s[j] not in hashmap:
        hashmap[s[j]]= hashmap.get(s[j],0)+1
        while i<j and hashmap[s[j]]>1:
            hashmap[s[i]] = hashmap.get(s[i],0)-1
            i += 1
        # print(i, j)
        res = max(res, j-i+1)
    return res
```

#### **40 *最小的k个数 / 最大的k个数（快速排序，分治的思想）**

```python
class Solution:
    def getLeastNumbers(self, arr, k):
        if k>= len(arr):return arr
        return self.partition(arr, 0, len(arr)-1, k)

    def partition(self, arr, left, right, k):
        if left>=right:return
        pivot = arr[left]
        l,r = left,right
        while l<r:
            while l<r and arr[r]>=pivot:r-=1
            arr[l] = arr[r]
            while l<r and arr[l]<=pivot:l+=1
            arr[r] = arr[l]
        arr[l] = pivot
        # return l
        if k<l: self.partition(arr, left, l-1, k)
        if k>l: self.partition(arr, l+1, right, k)
        return arr[:k]
```

#### 40-0 快排模板

```python
def quick_sort(nums, left, right):
    # 当只传来一个元素
    if left>=right:return
    pivot = nums[left]
    i,j = left, right
    while i<j:
        while i<j and nums[j]>=pivot:j-=1 # #从后往前查找，直到找到一个比pivot更小的数
        nums[i] = nums[j] # #将更小的数放入左边
        while i<j and nums[i]<=pivot:i+=1 # #从前往后找，直到找到一个比pivot更大的数
        nums[j] = nums[i] # #将更大的数放入右边
    # 循环结束，i与j相等
    nums[i] = pivot # 待比较数据放入最终位置
    # return i # 回待比较数据最终位置
    quick_sort(nums, left, i-1)
    quick_sort(nums, i+1, right)
    # print(nums)
```

#### **51 数组中的逆序对（归并排序）**

```python
def reversePairs(self, nums):
    self.res = 0
    return self.merge(nums, 0, len(nums)-1)

def merge(self, nums, l, r):
    if l>=r:return 0
    mid = (l+r)//2

    res = self.merge(nums, l, mid) + self.merge(nums, mid+1, r)
    # a = self.merge(nums, l, mid)
    # b = self.merge(nums, mid+1, r)
    # print("a+b", a, b)
    i, j = l, mid+1
    temp = []
    while i<=mid and j<=r:
        if nums[i] <= nums[j]: # 如果左边<=右边，不构成逆序对
            temp.append(nums[i])
            i += 1
        else:
            temp.append(nums[j])
            j += 1
            res += mid-i+1
    temp += nums[i:mid + 1]
    temp += nums[j:r + 1]

    # 把临时数组的元素再放回去，实现原地更改
    for k in range(r-l+1):
        nums[l+k] = temp[k]
    # k = l
    # for x in temp:
    #     nums[k] = x
    #     k+=1
    print("temp", temp)
    return res
```

#### 51-0 归并排序模板

```python
def merge_sort2(nums, l, r):
    if l>=r: return
    mid = (l+r)//2
    merge_sort2(nums, l, mid)
    merge_sort2(nums, mid+1, r)
    left_p, right_p = l, mid+1
    res = []
    while left_p <= mid and right_p <= r:
        if nums[left_p]<nums[right_p]:
            res.append(nums[left_p])
            left_p += 1
        else:
            res.append(nums[right_p])
            right_p += 1
    res += nums[left_p:mid+1]
    res += nums[right_p:r+1]
    # 把临时数组里的元素再放回去
    for k in range(r-l+1):
        nums[l+k] = res[k]
    # print("nums", nums)
    # print("res", res)
    # print('-'*20)
    return nums # nums已经实现原地更改
```

#### 57-2 和为s的连续正数序列（同向双指针）

```python
def findContinuousSequence(self, target):
    j = 1 # right 右端点
    s = 1 # 序列和
    res = []
    for i in range(1, target):
        # 当i固定时，right最远的点
        while s<target:
            j+=1
            s+=j
        # print(i,j, s)
        if s==target and j-i+1>1:
            path = []
            for k in range(i, j+1):
                path.append(k)
            res.append(path[:])
        s -= i
    return res
```



## 3【二分】

#### 04 二维数组中的查找

```python
def findNumberIn2DArray(self, matrix, target):
    if not matrix or not matrix[0]:return False
    n = len(matrix)
    m = len(matrix[0])
    i = 0
    j = m-1
    while i<n and j>=0:
        if matrix[i][j]==target:return True
        elif matrix[i][j]>target:j-=1
        else: i+=1
    return False
```

#### **11 *旋转数组的最小值 / 旋转数组的最大值**

```python
# 输入：[3,4,5,1,2]
# 输出：1
def minArray(self, numbers):
    # numbers是原本是递增的
    n = len(numbers)-1
    while(n>0 and numbers[n]==numbers[0]): n-=1
    # 最后比第一个值大，则一定递增
    if numbers[n] >= numbers[0]:return numbers[0]
    l, r = 0, n
    while(l<r):
        mid = (l+r)//2
        if numbers[mid]<numbers[0]: r=mid
        else:
            l = mid+1
    return numbers[l]
```

#### 53 *在排序数组中查找数字

```python
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: 2
def search_hash(self, nums, target):
    if not nums:return 0
    hashmap = {}
    for x in nums:
        hashmap[x] = hashmap.get(x,0)+1
    return hashmap.get(target,0)

def search(self, nums, target):
    if not nums:return 0
    # 二分出左边界
    l,r = 0,len(nums)-1
    while l<r:
        mid = (l+r)//2
        if nums[mid]<target:l=mid+1
        else: r = mid
    if nums[l] != target:return 0 # 重要!
    start = l

    l, r = 0, len(nums) - 1
    while l<r:
        mid = (l+r+1)//2
        if nums[mid]>target:r=mid-1
        else: l=mid
    if nums[l] != target:return 0 # 重要！
    end = l
    # print(start,end)
    return end-start+1
```

#### 53-2 0~n-1中缺失的数字

```python
# 输入: [0,1,3]
# 输出: 2
def missingNumber1(self, nums):
    n = len(nums)+1
    s = (0+n)*(n-1)//2
    for x in nums:
        s -= x
    return s

def missingNumber(self, nums):
    l,r = 0,len(nums)-1
    while l<r:
        mid = (l+r)//2
        if nums[mid]==mid:l=mid+1
        else:r=mid
    return l
```



## 4【链表】

> 特别声明：凡是可能将头节点删除的，都需要建立虚拟节点dummy。
> **删除重复节点 2个指针（dummy、p、q）**
>
> - p：重复节点前的第一个位置。p.next=q
> - q：不重复节点的第一个位置。
>
> **翻转链表 3个指针（prev、cur、tail）**
>
> - cur：当前操作节点。
> - prev：一开始为空，因为链表尾部为空，cur的上一个节点。
> - tail：cur节点的下一位，防止丢失。
>
> **删除链表 1个指针（p = dummy）**

#### 06 从尾到头打印链表 easy

```python
def reversePrint(self, head: ListNode) -> List[int]:
	res = []
  while head:
     res.append(head.val)
     head = head.next
  return res[::-1]
```

#### 18 删除链表的节点 easy

```python
def deleteNode(self, head: ListNode, val: int) -> ListNode:
    if not head:return head
    dummy = ListNode(-1)
    dummy.next = head
    p = dummy
    while p.next:
        if p.next.val == val:
            p.next = p.next.next
            return dummy.next
        p = p.next
    return dummy.next
```

#### 22 链表中倒数第k个节点 easy

```python
def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
    p = head
    lens = 0
    while p:
        lens += 1
        p = p.next

    n = lens - k + 1
    p = head
    for i in range(1, n):
        p = p.next
    return p
```

#### **24 *反转链表** easy

```python
def reverseList(self, head):
    if not head or not head.next: return head
    # 反转链表需要3个节点
    prev = None
    cur = head
    while cur:
        tail = cur.next
        cur.next = prev
        prev = cur
        cur = tail
    # self.print_link(prev)
    return prev
```

#### 25 合并两个排序链表 easy

```python
def mergeTwoLists(self, l1, l2):
    head = ListNode(-1)
    p = head
    p1 = l1
    p2 = l2
    while p1 and p2:
        if p1.val <= p2.val:
            p.next = p1
            p1 = p1.next
        else:
            p.next = p2
            p2 = p2.next
        p = p.next

    if p1:
        p.next = p1
    elif p2:
        p.next = p2

    self.printList(head.next)
    return head.next
```

#### 35 复杂链表的复制 middle

```python
def copyRandomList(self, head):
    if not head: return head
    cur = head
    # 1. 复制各节点，并构建拼接链表
    while cur:
        fake = Node(cur.val)
        fake.next = cur.next
        cur.next = fake
        cur = fake.next
        # 成z字

    # 2. 构建各新节点的 random 指向
    p = head
    while p:
        # 注意这里有random节点才改变
        if p.random:
            p.next.random = p.random.next
        p = p.next.next

    # 3. 拆分两链表
    pre = head # 指向旧链表
    cur = head.next # 指向新链表
    res = head.next # 指向新链表
    while cur.next:
        pre.next = pre.next.next # 删除旧与新的连接
        cur.next = cur.next.next
        pre = pre.next
        cur = cur.next
    # pre.next = None  # 单独处理原链表尾节点
    return res
```

#### 52 两个链表的第一个公共节点 easy

```python
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    pa, pb = headA, headB
    while pa!=pb:
        pa = pa.next if pa else headB
        pb = pb.next if pb else headA
    return pa
```



## 5【树】

#### 07 重建二叉树

```python
class Solution:
    def __init__(self):
        self.hash_map = {}

    def buildTree(self, preorder, inorder):
        self.preorder = preorder
        self.inorder = inorder
        # 快速在中序遍历中，找到某个值的下标
        for i, val in enumerate(inorder):
            self.hash_map[val] = i
        return self.dfs(0, len(preorder)-1, 0, len(inorder)-1)

    def dfs(self, pl, pr, il, ir):
        if pl>pr:return None # dfs一定要有循环的出口
        root = TreeNode(self.preorder[pl])
        k = self.hash_map[self.preorder[pl]]
        # 去前序遍历中找左子树，去中序遍历中找左子树
        root.left = self.dfs(pl+1, pl+k-il, il, k-1)
        # 去前序遍历中找右子树，去中序遍历中找右子树
        root.right = self.dfs(pl+k-il+1, pr,k+1, ir)
        return root
```

#### 26 树的子结构

```python
class Solution(object):
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        # 空树不是任意一个树的子结构
        if not A or not B: return False
        if self.is_part(A, B): return True
        return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

    def is_part(self, p1, p2):
        if not p2: return True
        if not p1: return False
        if p1.val != p2.val: return False
        return self.is_part(p1.left, p2.left) and self.is_part(p1.right, p2.right)
```

#### 27 二叉树的镜像

```python
class Solution(object):
    # 递归
    def mirrorTree(self, root):
        if not root: return root
        root.right = self.mirrorTree(root.right)
        root.left = self.mirrorTree(root.left)
        root.right, root.left = root.left, root.right
        return root

    # 遍历
    def mirrorTree2(self, root: TreeNode) -> TreeNode:
        if not root: return root
        queue = [root]
        while queue:
            node = queue.pop()
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
            node.left, node.right = node.right, node.left
        return root
```

#### 28 对称的二叉树

```python
class Solution:
    def isSymmetric(self, root):
        # 如果是空树，则是对称二叉树
        if not root:return True
        return self.dfs(root.left, root.right)

    def dfs(self, p, q):
        # 如果有一边为空，则返回结果
        if not p or not q:
            return not p and not q
        if p.val != q.val: return False
        return self.dfs(p.left, q.right) and self.dfs(p.right, q.left)
```

#### **32-1 从上到下打印二叉树**

#### **32-3 *z字从上到下打印二叉树**

```python
class Solution(object):
    # [3,9,20,15,7]
    def levelOrder1(self, root):
        if not root:return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            tmp = queue.pop(0)
            res.append(tmp.val)
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return res

    # [[3], [9,20], [15,7]]
    def levelOrder2(self, root):
        if not root:return []
        queue = []
        res = []
        queue.append(root)
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                tmp = queue.pop(0)
                cur_level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            res.append(cur_level[:])
        return res

    # 之字形遍历
    # [[3], [20,9], [15,7]]
    def levelOrder3(self, root):
        if not root:return []
        queue = []
        res = []
        queue.append(root)
        flag = 1
        while queue:
            cur_level, size = [], len(queue)
            for i in range(size):
                tmp = queue.pop(0)
                cur_level.append(tmp.val)
                if tmp.left:
                    queue.append(tmp.left)
                if tmp.right:
                    queue.append(tmp.right)
            res.append(cur_level[::flag])
            flag *= -1
        return res
```

#### 33 二叉搜索树后续遍历

```python
class Solution:
    # RecursionError: maximum recursion depth exceeded.
    # python的递归深度是有限制的，默认为1000
    def verifyPostorder1(self, postorder):
        self.postorder = postorder
        return self.dfs(0, len(postorder) - 1)

    def dfs(self, l, r):
        # 定义dfs的出口
        if l >= r: return True
        root = self.postorder[r]
        k = l
        while k < r and self.postorder[k] < root: k += 1
        mid = k
        while self.postorder[k] > root: k += 1
        return k == r and self.dfs(l, mid - 1) and self.dfs(mid, r - 1)
        
### 方法2
    def verifyPostorder(self, postorder):
        def dfs(l, r):
            if l >= r: return True
            k = l
            while postorder[k] < postorder[r]: k += 1
            m = k
            while postorder[k] > postorder[r]: k += 1
            return k == r and dfs(l, m - 1) and dfs(m, r - 1)

        return dfs(0, len(postorder) - 1)
```

#### 34 二叉树中和为某一值的路径

```python
class Solution:
    def pathSum(self, root: TreeNode, target):
        res = []
        if not root:return res
        self.dfs(res, [], root, target)
        return res

    def dfs(self, res, path, root, target):
        # 定义dfs出口
        if not root: return
        path.append(root.val)
        target -= root.val
        # 一定要是叶子节点，才算走到了末尾。并且target为0
        if not root.left and not root.right and target==0:
            res.append(path[:])
        self.dfs(res, path, root.left, target)
        self.dfs(res, path, root.right, target)
        # 1_回溯算法
        path.pop()
```

#### 36 二叉搜索树与双向链表

```python
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        self.pre = None
        self.dfs(root)
        self.head.left, self.pre.right = self.pre, self.head # right、left可以修改的
        return self.head

    def dfs(self, cur):
        if not cur: return
        self.dfs(cur.left)  # 递归左子树
        if self.pre:  # 修改节点引用
            self.pre.right, cur.left = cur, self.pre # right、left可以修改的
        else:  # 记录头节点
            self.head = cur
        self.pre = cur  # 保存 cur
        self.dfs(cur.right)  # 递归右子树
```

#### 37 序列化二叉树

```python
class Codec:
    # 1,2,3,#,#,4,5
    def serialize(self, root): # 将树转为list(层次遍历)
        if not root:return "#"
        queue = [root]
        ans = []
        while queue:
            node = queue.pop(0)
            if not node:
                ans.append('#')
            else:
                ans.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        while ans and ans[-1] == '#':
            ans.pop()
        return ','.join(ans)

    def deserialize(self, data): # 还原树
        root_nums = data.split(',')
        if not root_nums or root_nums[0]=='#' or root_nums[0]=='':
            return None
        root = TreeNode(int(root_nums.pop(0)))
        is_left = True # 当前节点该连左子树or右子树
        cur_node = root # 当前节点
        tree_node = [] # 已经连接的节点，为了找到下一个最左节点
        while root_nums:
            num = root_nums.pop(0)
            if is_left:
                is_left = False
                if num != '#':
                    cur_node.left = TreeNode(int(num))
                    tree_node.append(cur_node.left)
            # 开始右节点
            else:
                is_left = True
                if num != '#':
                    cur_node.right = TreeNode(int(num))
                    tree_node.append(cur_node.right)
                cur_node = tree_node.pop(0)
        return root
```

#### 54 二叉搜索树的第k大节点

```python
class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        if not root: return 0
        self.k = k
        self.dfs(root)
        return self.res
    # 注意这里 k 需要是全局变量。
    def dfs(self, root):
        if not root:return
        # 右根左遍历
        self.dfs(root.right)
        if self.k==0:return
        self.k-=1
        if self.k==0:self.res=root.val
        self.dfs(root.left)
```

#### 55-1 二叉树的深度

```python
def maxDepth(self, root: TreeNode) -> int:
    if not root:return 0
    left = self.maxDepth(root.left)
    right = self.maxDepth(root.right)
    return max(left, right)+1
```

#### 55-2 平衡二叉树

```python
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:return True
        return abs(self.depth(root.left) - self.depth(root.right)) <= 1 and \
               self.isBalanced(root.left) and self.isBalanced(root.right)

    # 计算每个节点的深度
    def depth(self, root):
        # 定义dfs的出口
        if not root:return 0
        right = self.depth(root.right)
        left = self.depth(root.left)
        return max(right, left)+1
```

#### **68-1 二叉搜索树的最近公共祖先**

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if not root:return root
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
```

#### 68-2 *二叉树的最近公共祖先

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:return root
        if root==p or root==q:return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:return root
        if left: return left
        return right
```



## 6【dp动态规划】

#### 10 斐波那契数列

```python
# 求斐波那契（Fibonacci）数列的第 n 项（即 F(N)）
def fib(self, n):
    if n==0:return 0
    if n==1:return 1
    dp = [0 for _ in range(n+1)]
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = (dp[i-1]+dp[i-2])% 1000000007
    return dp[n]
```

#### 10 青蛙跳台阶问题

```python
def numWays(self, n: int):
    if n==0:return 1
    if n==1:return 1
    dp = [1 for _ in range(n+1)]
    for i in range(2, n+1):
        dp[i] = (dp[i-1]+dp[i-2])%1000000007
    return dp[n]
```

#### 19 正则表达式匹配

```python
def isMatch(self, s: str, p: str):
    n = len(s)
    m = len(p)
    dp = [[False for _ in range(m+1)] for _ in range(n+1)] # n行m列
    dp[0][0] = True # 空串和空模式串是匹配的， 空模式串和任意的
    for i in range(n+1):
        for j in range(m+1):
            if j == 0:
                dp[i][j] = i == 0
            else:
            # 非空正则分为两种情况 * 和 非*
                if p[j-1] != '*':
                    if i>0 and ((s[i-1]==p[j-1]) or p[j-1]=='.'):
                        dp[i][j] = dp[i-1][j-1]
                else:
                    # 不看
                    if j>=2:
                        dp[i][j] |= dp[i][j-2]
                    # 看
                    if i>=1 and j>=2 and ((s[i-1] == p[j-2]) or p[j-2]=='.'):
                        dp[i][j] |= dp[i-1][j]
    # print(dp)
    return dp[-1][-1]
```

#### 42 *连续子数组最大和

```python
class Solution:
    # dp[i] 以i结尾的连续子数组的最大和
    def maxSubArray(self, nums) -> int:
        n = len(nums)
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
        # print(dp)
        return max(dp)
```

#### 46 把数字翻译成字符串

```python
# 状态定义：设动态规划列表 dp ，dp[i] 代表以 nums[x_i+1] 为结尾的数字的翻译方案数量。
class Solution:
    def translateNum(self, num):
        s = str(num)
        dp = [0 for _ in range(len(s)+1)]
        # print(len(s)) # 5
        # print(len(dp)) # 6
        dp[0] = 1 #
        dp[1] = 1 # 第 1 位数字,nums[0] 的翻译方法数量为 1
        for i in range(2, len(dp)):
            tmp = s[i-2:i]
            if int(tmp)<=25 and int(tmp)>=10:
                dp[i] = dp[i-1]+dp[i-2]
            else:
                dp[i] = dp[i-1]
        # print("dp", dp)
        return dp[len(s)]
```

#### 47 礼物的最大价值

```python
# 设 f(i, j)n为从棋盘左上角走至单元格 (i,j) 的礼物最大累计价值
class Solution:
    def maxValue(self, grid):
        if not grid and not grid[0]:return 0
        m = len(grid)
        n = len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        # 初始化
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0]+grid[i][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1]+grid[0][j]
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])+grid[i][j]
        return dp[m-1][n-1]
```

#### 49 丑数

```python
class Solution:
    def nthUglyNumber(self, n):
        dp = [1]*n
        a,b,c = 0,0,0
        for i in range(1,n):
            n2,n3,n5 = dp[a]*2,dp[b]*3,dp[c]*5
            dp[i] = min(n2,n3,n5)
            if dp[i]==n2:a+=1
            if dp[i]==n3:b+=1
            if dp[i]==n5:c+=1
        return dp[-1]
```

#### ~~60 n个骰子的点数 dp~~

#### 63 股票的最大利润

```python
# dp[i] 为 第i天卖出的最大利润
# 扩展可以交易两次（买卖算一次交易）求最大值
class Solution:
    def maxProfit(self, prices):
        if not prices:return 0
        dp = [0 for _ in range(len(prices))]
        cost = prices[0]
        for i in range(1, len(prices)):
            cost = min(cost, prices[i])
            dp[i] = max(dp[i-1], prices[i]-min(cost, prices[i]))
        return max(dp)
```



## 7【栈 & 队列】

#### 09 用两个栈实现队列

```python
class CQueue:
    def __init__(self):
        self.stk1 = [] # 进栈
        self.stk2 = [] # 出栈

    # 队列尾部插入整数
    def appendTail(self, value):
        self.stk1.append(value)

    # 在队列头部删除整数
    def deleteHead(self):
        if self.stk2: return self.stk2.pop()
        if not self.stk1: return -1
        while self.stk1:
            self.stk2.append(self.stk1.pop())
        return self.stk2.pop()
```

#### 30 包含min函数的栈

```python
class MinStack:
    def __init__(self):
        self.stk, self.min_stk = [], []

    # 注意这里，=也要包含进去
    def push(self, x: int) -> None:
        self.stk.append(x)
        # if not self.min_stk: self.min_stk.append(x)
        # else:
        #     if x<self.min_stk[-1]:
        #         self.min_stk.append(x)
        if not self.min_stk or self.min_stk[-1] >= x:
            self.min_stk.append(x)

    def pop(self) -> None:
        if self.stk.pop() == self.min_stk[-1]:
            self.min_stk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def min(self) -> int:
        return self.min_stk[-1]
```

#### 31 栈的压入、弹出序列

```python
class Solution:
    def validateStackSequences(self, pushed, popped) -> bool:
        stk = []
        i = 0 # 标记popped顺序
        for x in pushed:
            stk.append(x)
            while stk and stk[-1]==popped[i]:
                stk.pop()
                i += 1
        return not stk
```

#### **59 *滑动窗口最大值（单调栈）**

```python
class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or not k:return []
        stk = []
        res = []
        for i in range(len(nums)):
            # 比当前元素小的数据都干掉
            while stk and nums[i]>nums[stk[-1]]:
                stk.pop()

            # # 超过窗口范围，队首元素出队
            while stk and i-k>=stk[0]:
                stk.pop(0)

            stk.append(i)
            # print(i, stk)
            if i+1>=k:
                res.append(nums[stk[0]])
        return res
```

#### 59-2 队列的最大值

```python
class MaxQueue:
    def __init__(self):
        self.q = []
        self.max_q = []

    def max_value(self) -> int:
        if not self.max_q:return -1
        return self.max_q[0]
    # return self.max_q.pop(0) 这样就探弹出去了

    def push_back(self, value: int) -> None:
        self.q.append(value)
        while self.max_q and value>self.max_q[-1]:
            self.max_q.pop() # 注意这里是左边
        self.max_q.append(value)

    def pop_front(self) -> int:
        if not self.q:return -1
        tmp = self.q.pop(0)
        if self.max_q and tmp==self.max_q[0]:
            self.max_q.pop(0)
        return tmp
```



## 8【DFS & BFS】

> bfs是存在所有可行解
> dfs是有没有，dfs才需要回溯？
>
> bfs每个点只能访问一次，需要维护visited数据（判重数据）。
> bfs要维护队列。

#### 12 *矩阵中的路径 

**dfs 存不存在某一个值**

```python
class Solution:
    def exist(self, board, word):
        if not board or not board[0]:return False
        if not word: return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(word, board, 0, i, j):return True
        return False

    def dfs(self, word, board, u, x, y):
        """
        :param word: 原始target单词
        :param board: 原始matrix数组
        :param u: 定位target
        :param i: 定位matrix
        :param j: 定位matrix
        :return:
        """
        if board[x][y] != word[u]: return False
        if len(word)-1 == u: return True
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        tmp = board[x][y]
        board[x][y] = '*'
        for i in range(4):
            a = x+dx[i]
            b = y+dy[i]
            if a>=0 and a<len(board) and b>=0 and b<len(board[0]):
                if self.dfs(word, board, u+1, a, b):return True
        board[x][y] = tmp
        return False
```

#### 13 *机器人的运动范围 

**bfs 所有可行解**

```python
class Solution:
    def get_sum(self, n):
        s = 0
        while n:
            s += n%10
            n //= 10
        return s

    def movingCount(self, m, n, k):
        if not m and not n: return 0
        res = 0
        visited = [[False for _ in range(n)] for _ in range(m)]
        queue = []
        queue.append((0, 0))
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        while queue:
            tmp = queue.pop(0)
            if self.get_sum(tmp[0])+self.get_sum(tmp[1])>k or visited[tmp[0]][tmp[1]]:continue
            res += 1
            visited[tmp[0]][tmp[1]] = True
            for i in range(4):
                a = tmp[0]+dx[i]
                b = tmp[1]+dy[i]
                if a>=0 and a<m and b>=0 and b<n and not visited[a][b]:
                    queue.append((a,b))
        return res
```

#### 29 顺时针打印矩阵

```python
class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]: return matrix
        res = []
        n = len(matrix)
        m = len(matrix[0])
        dx = [-1,0,1,0]
        dy = [0,1,0,-1]
        x,y,d = 0,0,1
        visited = [[False for _ in range(m)] for _ in range(n)]
        for i in range(n*m):
            res.append(matrix[x][y])
            visited[x][y] = True
            a = x+dx[d]
            b = y+dy[d]
            if a<0 or a>=n or b<0 or b>=m or visited[a][b]:
                d = (d+1)%4
                a = x + dx[d]
                b = y + dy[d]
            x = a
            y = b
        return res
```

#### 38 *字符串的排列 dfs

```python
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
class Solution:
    # ['acb', 'bca', 'cba', 'abc', 'bac', 'cab']
    def permutation(self, s: str):
        res = []
        if not s: return res
        self.dfs("", res, s)
        return list(set(res))

    def dfs(self, path, res, s):
        # 定义dfs出口
        if s == '': res.append(path)
        # 轮流当首字母
        for i in range(len(s)):
            self.dfs(path + s[i], res, s[:i] + s[i + 1:])
        return res
```



## 9【位运算】

#### 15 二进制中1的个数

```python
class Solution:
    def hammingWeight(self, n):
        res = 0
        for i in range(32):
            res += n&1
            n = n>>1
        return res
```

#### 56-1 数组中数字出现的次数2次

```python
def singleNumbers(self, nums):
    n = 0
    for num in nums:         # 1. 遍历异或
        n ^= num
    # print(n) # 7
    # 获取x^y的首位1出现的位置
    # x 和 y 的此m二进制位一定不同
    m = 1 # 现在不同的位置是右边第一位
    while n&m ==0:           # 2. 循环左移，计算 m
        m <<= 1
    x,y=0,0
    for num in nums:          # 3. 遍历 nums 分组
        if num & m: x ^= num  # 4. 当 num & m != 0
        else: y ^= num        # 4. 当 num & m == 0
    return [x,y]
```

#### 56-2 数组中数字出现的次数3次

```python
```

#### 65 不用加减乘除做加法

```python

```



## 10【其他】

14 剪绳子1（）

14 剪绳子2（）

16 数值的整数次方（快速幂）

~~17 打印从1到最大的n位数（大数问题 模拟题）~~

20 表示数值的字符串（模拟题）

67 把字符串转成整数（模拟题）

41 数据流中的中位数 （堆）

43 1~n整数中1出现的次数hard（数位dp，递归，数学模拟）

44 数字序列中某一位的数字（找规律）

45 把数组排成最小的数（python内置排序函数）

61 扑克牌中的顺子（）

62 圆圈中最后剩下的数字（约瑟夫环）

64 求1+2..+n（逻辑and or）

66 构建乘积数组（模拟题）







# 2. 记录

【2021-07-13】(看笔记之后做题，仍有问题) 3 10 11 

剑指 Offer 03 [数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof)

关于数值交换，踩坑 [交换列表中的两个值遇到的坑](https://blog.csdn.net/weixin_39544046/article/details/105972357)

剑指 Offer 11 [旋转数组的最小数字](https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/)

剑指 Offer 10- II [青蛙跳台阶问题](https://leetcode-cn.com/problems/qing-wa-tiao-tai-jie-wen-ti-lcof/)

**由于 Python 中整形数字的大小限制 取决计算机的内存 （可理解为无限大），因此可不考虑大数越界问题。**

----

【2021-07-14 ~ 2021-07-15】
- 剑指 Offer 16 [数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/solution/mian-shi-ti-16-shu-zhi-de-zheng-shu-ci-fang-kuai-s/)

- 13 bfs 所有可行解

考察快速幂的概念

20 模拟题（不用二刷了）

[位运算相关题目](https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/solution/gong-shui-san-xie-yi-ti-si-jie-wei-shu-j-g9w6/)


位运算15、快速幂16

---

26、28

[剑指 Offer 28. 对称的二叉树](https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/solution/mian-shi-ti-28-dui-cheng-de-er-cha-shu-di-gui-qing/)

[二叉树对称性递归题目汇总](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/solution/yi-pian-wen-zhang-dai-ni-chi-tou-dui-che-uhgs/)

13、16、18、29、31

> 14-20没做, 18想7月16日早上自己做一下

----

33、34、38 需要重做

35 error

剑指 Offer 39. 数组中出现次数超过一半的数字 | 摩尔投票法

----

40 最小的 k 个数 (必会!!!)

45 python自定义函数的定义

> 比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0。

46 一维dp，需要重做

48 同向双指针，最长不含重复字符的子字符串，必回!!!

49 一维dp，需要重做

53 二分，需要重做

54 bst，需要重做
> 排序数组中的搜索问题，首先想到 二分法 解决。

55 二叉树的深度 once ok

58 once okk


---



辣鸡题目

20. 表示数值的字符串
