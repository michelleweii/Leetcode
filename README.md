常用网站：

1. [企业题库](https://codetop.cc/home)

2. [代码随想录](https://programmercarl.com/)

# 1、二叉树
## 1.1、层次遍历
- 102.二叉树的层序遍历（已完成）
- 103.[二叉树的锯齿形层序遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal)  （已完成）
- 二叉树的右视图
- 二叉树的层平均值
- N叉树的前序遍历
- 在每个树行中找最大值
- 填充每个节点的下一个右侧节点指针
- 117.[填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii) （已完成，链表+层次遍历）
- 208 前缀树(字典树概念) 重做！！！

二叉搜索树：对于树中每个节点,
若其左子树存在，则其左子树中每个节点的值都不大于该节点值；
若其右子树存在，则其右子树中每个节点的值都不小于该节点值。

BST的中序遍历是升序的。

lc113: 找到所有路径，所以递归函数不要返回值！

# 2、二分和单调队列
## 2.1、二分
- 153.旋转数组最小值0513
- 162.寻找峰值0513

## 2.2、单调队列
- 496 下一个更大元素 I (模板题)
- 42 接雨水（单调栈，还是不会）
- 84 柱状图中最大的矩形（单调栈）失败ing
单调栈模板
外面for循环，里面while循环。
**单调栈84 (双端添加哨兵)**、739、496、42

> **滑动窗口算法一定是双指针算法；**
>
> **双指针算法不一定是滑动窗口算法；**

# 3、字符串相关
- 686 KMP算法-middle

- 49 hash表 value是list[]

- 151 error

- 6 **zip()的使用以及边界**

- 无重复字符的最长子串

    > - **子串一定的是连续的；**
    > - **子序列不一定是连续的一段，但是下标要求是递增的；**
    > - **子数组（子数组最少包含一个元素）**

# 4、双指针
## **4.1、单向**

[https://www.bilibili.com/video/BV1P7411L7eV?from=search&seid=16847300039480678482](同向双指针（一）)
[https://www.bilibili.com/video/BV1P7411L7NK](同向双指针（二）)
[https://www.bilibili.com/video/BV1M741147Ta](双指针基础（一）)
[https://www.bilibili.com/video/BV1A7411L7EQ?from=search&seid=16847300039480678482](双指针基础（二）)

## **4.2、双向**

- 75 荷兰国旗问题
https://leetcode-cn.com/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/
题解这里，关于窗口的开闭是很重要的。

- 80 

### 需要重做
- easy 7
- middle 260 hash
- middle 29 位运算
- middle 43 没做
- middle 71 堆栈
- hard 30 0530没做

# 5、dp

416. 分割等和子集——动态规划之01背包问题
494. 目标和——动态规划之01背包问题
322. 零钱兑换——动态规划之完全背包问题
518. 零钱兑换 II——动态规划之完全背包的组合问题
377. 组合总和 Ⅳ——动态规划之完全背包考虑顺序的组合问题


https://www.bilibili.com/video/BV1hf4y197w3
https://www.bilibili.com/video/BV1CD4y127CZ
https://www.bilibili.com/video/BV1sk4y1y7Dv
https://www.bilibili.com/video/BV12k4y127nP
https://www.bilibili.com/video/BV14z4y1f7hH


# 6、链表

148. 排序链表【如何寻找一个链表的中间点】与876的差别在哪？

快慢指针找到中点的时候，快指针最开始一定要设置为head.next，设置成head就会栈溢出.

使用 fast,slow 快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。中点 slow。
```
如果slow = fast = head,那么在链表只剩两个节点的时候有以下执行顺序：(首节点->尾节点->null)
0. 执行查找中点的while循环
1. 得出：slow = 尾节点，fast = null
2. mid = slow.next;
   slow.next = null; 
   //第2步为断链,需要注意的是,slow的next原本就是null(由第1步得出)
   //也就是说,断链操作根本没有生效,链表结构依然是:首节点->尾节点->null
3. 进入递归,由于链表结构没变,所以会继续进行查找中点、断链操作,重复以上步骤,导致栈溢出
-----------------------------------------------------------
如果slow = head,fast = head.next,那么在链表只剩两个节点的时候有以下执行顺序：(首节点->尾节点->null)
0. 执行查找中点的while循环
1. 得出：slow = 首节点，fast = 尾节点
2. mid = slow.next;
   slow.next = null; 
   //这里的断链操作生效了,此时链表结构为：首节点->null,尾节点->null
3. 进入递归,重复以上步骤,此时的链表已经分解成两个节点,所以不会查找中点及断链,而是直接return。
```

优雅求一个链表的长度`while h: h, length = h.next, length + 1`


# 重要算法

- 214 最短回文数（KMP算法）
- 208 （字典树/前缀树）
- 





特别地

- float("inf") #Python中可以用如下方式表示正负无穷：float("inf"), float("-inf")

- lc31 对sort切片有了新的理解



> 283、1047关于原地覆盖的问题，需要多次回顾。


134 for循环适合模拟从头到尾的遍历，而while循环适合模拟环形遍历，要善于使用while！



待做

- [ ] 214 kmp hard

- [ ] 30 双指针 hard


定义一个最大数 `dp=[sys.maxsize]*len(s)`

2021年10月12日回归呜呜

一个无向图，需要用标记位，标记着节点是否走过，否则就会死循环！





# 10、top200未做题目

- [ ] 152 middle
- [ ] 154 hard 二分
- [ ] 155 easy 单调栈
- [ ] 164 hard 基数排序
- [ ] 166 middle 竖式除法
- [ ] 173 middle
- [ ] 174 hard ()
- [ ] 179 middle
- [ ] 189 middle

【sql】

- [ ] 176 middle

- [ ] 177 middle

- [ ] 178 middle

- [ ] 180 middle
- [ ] 184 middle
- [ ] 185 hard

【bash】

- [ ] ß192 middle
- [ ] 194 middle