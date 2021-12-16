常用网站：

1. [企业题库](https://codetop.cc/home)
2. [代码随想录](https://programmercarl.com/)
2. [刷题模板](https://fuxuemingzhu.blog.csdn.net/article/details/101900729)

题目关键字：

【dp关键字】能不能组成True or False、有多少种

【dfs关键字】打印所有结果（回溯）

【】前缀和~=hashmap

# 1. 二叉树

[bitree题目集合](https://leetcode-cn.com/problems/convert-bst-to-greater-tree/solution/yi-tao-quan-fa-shua-diao-nge-bian-li-shu-de-wen-5/)

[树的遍历（递归+迭代）](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/die-dai-fa-by-jason-2/)

## 1.1. 层次遍历
- 102.二叉树的层序遍历（已完成）
- 103.[二叉树的锯齿形层序遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal)  （已完成）
- 二叉树的右视图
- 二叉树的层平均值
- N叉树的前序遍历
- 在每个树行中找最大值
- 填充每个节点的下一个右侧节点指针
- 117.[填充每个节点的下一个右侧节点指针 II](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii) （已完成，链表+层次遍历）
- 208 前缀树(字典树概念) 重做！！！

lc113: 找到所有路径，所以递归函数不要返回值！

> 最大深度：从根节点到叶节点最长的那条路径上的节点数。
> 最大路径：任意两个节点最长的那条路径上的边数。
>
> 二叉搜索树（BST）：对于树中每个节点,
> 若其左子树存在，则其左子树中每个节点的值都不大于该节点值；
> 若其右子树存在，则其右子树中每个节点的值都不小于该节点值。
>
> 性质：BST的中序遍历是升序的。
>

# 2. 二分法
- 153.旋转数组最小值0513
- 162.寻找峰值0513

# 3. 字符串相关
- 686 KMP算法-middle

- 49 hash表 value是list[]

- 151 error

- 6 **zip()的使用以及边界**

- 无重复字符的最长子串

    > - **子串一定的是连续的；**
    > - **子序列不一定是连续的一段，但是下标要求是递增的；**
    > - **子数组（子数组最少包含一个元素）**

# 4. 双指针
**滑动窗口算法一定是双指针算法；双指针算法不一定是滑动窗口算法；**

## **4.1. 单向（滑动窗口）**

[https://www.bilibili.com/video/BV1P7411L7eV?from=search&seid=16847300039480678482](同向双指针（一）)
[https://www.bilibili.com/video/BV1P7411L7NK](同向双指针（二）)
[https://www.bilibili.com/video/BV1M741147Ta](双指针基础（一）)
[https://www.bilibili.com/video/BV1A7411L7EQ?from=search&seid=16847300039480678482](双指针基础（二）)

76：cnt元素维度，初始化是目标，每当window中包含一个，cnt--；

438：window中字符个数与目标保持一致，字符维度，flag++；

s长串、t短串，**两个while循环解决**。

```python
# 一般框架
"""
遍历s，求最小问题
    1、移动right，寻找可行解，满足t_tmp
        2、移动left，寻找最优解
"""
while right<len(s):
    # 当满足条件了，一般是hash表字符个数满足了
    while(根据题意，不用寻找最优解，就不用第二个while了)：
        left++
    right++
```



## **4.2. 双向**

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

# 5. dp

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


# 6. 链表

148. 排序链表【如何寻找一个链表的中间点】与876的差别在哪？

快慢指针找到中点的时候，快指针最开始一定要设置为head.next，设置成head就会栈溢出.

使用 fast,slow 快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。中点 slow。
```python
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



# 7. 单调栈

https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/solution/dan-diao-zhan-jie-fa-by-lilin-k-7096/

- 单调递减栈：从栈底到栈顶数据是从大到小；**<u>序列从大到小，比栈顶元素小直接入栈，比栈顶元素大，则将比当前元素小的所有元素都干掉，一直出栈，直到满足性质后，当前元素入栈；</u>**

​		<u>**- 找(一边)两边比cur大**</u>【核心！】

​       - 单调递减栈操作：如果栈为空或入栈元素值小于栈顶元素值，则入栈；否则，如果入栈则会破坏栈的单调	性，则需要把比入栈元素小的元素全部出栈。

- 单调递增栈：从栈底到栈顶数据是从小到大；<u>**序列从小到大，比栈顶元素大直接入栈，比栈顶元素小，则将比当前元素大的元素都干掉，一直出栈，直到满足性质后，当前元素入栈**</u>；

​		**<u> - 找(一边)两边比cur小</u>** 【核心！】

- 应用场景：

> 1.<u>需要找到两边（一边）比cur大（小）的值时可以用</u>，遇到时退栈并计算（更新），栈中一般存储下标（下标和值的pair，或值另外存在vector）
>
> 2.需要在无序数列中保证有序数列时，如去掉k位数使得数最小，此时栈中一般保存数而不是下标。

```c++
// 单调递增
for(int i = 0; i < nums.size(); i++){ //for循环
    while(!st.empty() && nums[i] < st.top()){ //while循环
      // 一些操作
}
     st.push(nums[i]);
}
```

> 哨兵：https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/bao-li-jie-fa-zhan-by-liweiwei1419/
>
> 需要考虑两种特殊的情况：1、弹栈的时候，栈为空；2、遍历完成以后，栈中还有元素；
> 为此可以我们可以在输入数组的两端加上两个高度为 0 （或者是 0.5，只要比 1 严格小都行）的柱形，可以回避上面这两种分类讨论。
>
> 这两个站在两边的柱形有一个很形象的名词，叫做哨兵（Sentinel）。
>
> 有了这两个柱形：
>
> - 左边的柱形（第 1 个柱形）由于它一定比输入数组里任何一个元素小，它肯定不会出栈，因此栈一定不会为空；
>- 右边的柱形（第 2 个柱形）也正是因为它一定比输入数组里任何一个元素小，它会让所有输入数组里的元素出栈（第 1 个哨兵元素除外）。

<u>逆序的单调栈</u>掌握不好：逆序的单调递减，指的是从后向前看数组的递减的。（就是正着看是递增啊）

- 42.接雨水（单调递减栈）# 先放入哨兵，在循环里就不用做非空判断 # <u>**找两边比cur大**</u>
- 84.柱状图中最大的矩形（单调递增栈，**双端添加哨兵**）# <u>**找两边比cur小**</u>
- 456.（单调栈逆序）
- 496.下一个更大元素 I 
- 581.
- 739.

# 8. 图

一个无向图，需要用标记位，标记着节点是否走过，否则就会死循环！

## 8.1. dfs



## 8.2. bfs



## 8.3. 并查集

作用：检查图中是否存在环，主要实现两个方法：

1. def find_root(x) # 找到x节点的根；
2. def union(x,y) # 将x，y节点进行合并（将x，y结点连起来）；

在并查集里，每个节点会记录它的父节点。

> 详解：https://leetcode-cn.com/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/

- 带权并查集

> https://leetcode-cn.com/problems/evaluate-division/solution/pythonbing-cha-ji-fu-mo-ban-by-milomusia-kfsu/
>
> 普通并查集只能判断两个元素是否在一个集合中，带权并查集可以维护集合元素之间的关系，这个关系由每个元素的权值维护。

四边形法则：https://www.cnblogs.com/enmac/p/13962764.html

四边形法则更新根节点的权重：`self.value[x_father] = self.value[y] * val / self.value[x]`

# pytrick

- float("inf") # Python中可以用如下方式表示正负无穷：float("inf"), float("-inf")。

- lc31 对sort切片有了新的理解。

- 定义一个最大数 `dp=[sys.maxsize]*len(s)`。

- **子串一定的是连续的；**
- **子序列不一定是连续的一段，但是下标要求是递增的；**
- **子数组（子数组最少包含一个元素），要求下标是连续的；**







> 283、1047关于原地覆盖的问题，需要多次回顾。

134 for循环适合模拟从头到尾的遍历，而while循环适合模拟环形遍历，要善于使用while！





# python语法

- 179 自定义比较函数
  sorted默认升序；修改reverse=True参数，改为降序；

- 切片

```python
nums = [1,2,3,4,5]
print(nums[:1]) # [1]
print(nums[:0]) # []
所以，nums[0:0] return 0
```



# 10、二进制性质

针对奇数有：二进制表示中，奇数一定比前面那个偶数多一个 1，因为多的就是最低位的 1。

```
# 举例：
#          0 = 0       1 = 1
#          2 = 10      3 = 11
```

针对偶数有：二进制表示中，偶数中 1 的个数一定和除以 2 之后的那个数一样多。因为最低位是 0，除以 2 就是右移一位，也就是把那个 0 抹掉而已，所以 1 的个数是不变的。

```
# 举例：
#           2 = 10       4 = 100       8 = 1000
#           3 = 11       6 = 110       12 = 1100
```

如果n是2的幂，则1）n 二进制最高位为 1，其余所有位为 0；2）n−1 二进制最高位为 0，其余所有位为 1；[refer](https://leetcode-cn.com/problems/power-of-two/solution/power-of-two-er-jin-zhi-ji-jian-by-jyd/)

| 2^x  | n    | n - 1 | n & (n - 1)          |
| ---- | ---- | ----- | -------------------- |
| 2^0  | 0001 | 0000  | (0001) & (0000) == 0 |
| 2^1  | 0010 | 0001  | (0010) & (0001) == 0 |
| 2^2  | 0100 | 0011  | (0100) & (0011) == 0 |
| 2^3  | 1000 | 0111  | (1000) & (0111) == 0 |

> 因此，通过 `n > 0` 且 `n & (n - 1) == 0` 即可判定是否满足 n = 2^x。



# 11、时间复杂度

判断字符是否在[栈]上存在需要 O(N) 的时间

判断字符是否在[hashmap]上存在需要 O(1) 的时间

查询给定字符是否在一个序列中存在的方法。根本上来说，有两种可能：
- 有序序列：可以二分法，时间复杂度大致是 O(logN)。

- 无序序列：可以使用遍历的方式，最坏的情况下时间复杂度为 O(N)。
  我们也可以使用空间换时间的方式，使用 N 的空间 换取 O(1)的时间复杂度——hashmap。

  


# 10、top200未做题目

- [ ] 164 hard 基数排序
- [ ] 166 middle 竖式除法

【sql】

- [ ] 176 middle

- [ ] 177 middle

- [ ] 178 middle

- [ ] 180 middle
- [ ] 184 middle
- [ ] 185 hard

【bash】

- [ ] 192 middle
- [ ] 194 middle

# 重要算法

- 214 最短回文数（KMP算法,hard）
- 208 （字典树/前缀树）
- 214 kmp 
- 

刷题时光轴

2021/10/12回归呜呜

2021/12/06