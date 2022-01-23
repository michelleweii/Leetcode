Fighting!

# 一维DP

明确概念，

- 数组：要求连续`i-1, i, i+1`;
- 子序列：不要求连续`i-3, i, i+5`;

dp套路，

- 单个数组或者字符串要用动态规划时，可以把动态规划 `dp[i]` 定义为 `nums[0:i]` 中想要求的结果；
- 当两个数组或者字符串要用动态规划时，可以把动态规划定义成两维的 `dp[i][j]` ，其含义是在 `A[0:i]` 与 `B[0:j]` 之间匹配得到的想要的结果。

### LC53.最大子序列和



### LC300.最长递增子序列



### LC673.最长递增子序列的个数



### LC198.打家劫舍



### LC213.打家劫舍2



### LC337.打家劫舍3







# 二维DP

大概分为一下几步，

1. 状态定义；
2. 定义出口；
3. 初始化边界；
4. 状态转移方程；

> 求方案数的基本都是相加的。

## 初始化

以[72. 编辑距离](https://leetcode-cn.com/problems/edit-distance/)为例，状态定义

```python
dp[i][j] 代表 word1 中前 i 个字符，变换到 word2 中前 j 个字符，最短需要操作的次数
```

一般都是表示前 i 个字符，前 j 个字符。e.g. 前5个字母，下标index=4。【这个错位一定要知道！】

初始化多申请一位的原因？

```python
m, n = len(word1), len(word2) # m行n列
dp = [[0] * (n + 1) for _ in range(m + 1)]
```

**考虑空字符串的因素，然后才是第一个字符到最后一个字符。**

删除一个元素`dp[i][j]=dp[i-1][j]+1`，

增加一个元素`dp[i][j]=dp[i][j-1]+1，`

替换一个元素`dp[i][j]=dp[i-1][j-1]`。

为什么是这样？因为题意要求从word1到word2，word1是可变的，word2是不可变的。

### LC72.编辑距离

状态定义：`dp[i][j] 代表 word1 中前 i 个字符，变换到 word2 中前 j 个字符，最短需要操作的次数`。

转移方程：

```python
dp = [[0] * (n+1) for _ in range(m+1)] # 多一位表示空字符
word1[i] == word2[j]，dp[i][j] = dp[i-1][j-1]
# 替换，删除，增加
word1[i] != word2[j]，dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
```

### LC97.交错字符串

[LC97.交错字符串](https://leetcode-cn.com/problems/interleaving-string/solution/dong-tai-gui-hua-zhu-xing-jie-shi-python3-by-zhu-3/) 题目：给定三个字符串 `s1`、`s2`、`s3`，请你帮忙验证 `s3` 是否是由 `s1` 和 `s2` **交错** 组成的。

`s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac", True.`

状态定义：`dp[i][j]表示 s1 的前i个(s1[i-1])个字符和s2的前j个(s2[j-1])字符是否能构成 s3 的前i+j个字符`。

转移方程：

s1的前i位和s2的前j位能否构成s3的前i+j(index=i+j-1)位，取决于2种情况：

1. s1最后一个字符和s3最后一个字符匹配；
2. s2最后一个字符和s3最后一个字符匹配；

```python
# 多初始化一维是为了放置空字符。
# dp[0][0] = True # s1的0个字符，s2的0个字符，当然可以构成s3的0个字符。

# 边界初始化
# 1、只由s1构成s3 # s1的前i位是否能构成s3的前i位
for i in range(1, len1+1):
  # s1的前i位能构成s3的前i位的前提条件是：
  # 前i-1位可以构成s3的前i-1位，且s1的第i位（s1[i-1]）等于s3的第i位（s3[i-1]）
  dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]

  # s1的前i位和s2的前j位能否构成s3的前i+j(index=i+j-1)位，取决于2种情况：
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        # s1 的前 i 个字符和 s2 的前 j−1 个字符能否构成 s3 的前 i+j−1 位，# （s1最后一个字符和s3最后一个字符匹配）
        # or s2 的第 j 位（s2[j−1]）是否等于 s3 的第 i+j 位（s3[i+j−1]）。# （s2最后一个字符和s3最后一个字符匹配）
        dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) \
        or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
```

### LC115.不同的子序列

[LC115.不同的子序列](https://leetcode-cn.com/problems/distinct-subsequences/solution/shou-hua-tu-jie-xiang-jie-liang-chong-ji-4r2y/)题目：给定一个字符串 `s` 和一个字符串 `t` ，计算在 `s` 的子序列中 `t` 出现的个数。翻译为**『在 s 串身上 “挑选” 字符，去匹配 t 串的字符，求挑选的方式数』**

状态定义：从0到 `s[i-1]` 的子串中，出现『从0到 `t[j-1]` 的子串』的 次数。**即，从 前者 选字符，去匹配 后者 的方案数**

转移方程：

```python
# dp出口
# 1) 小到 t 变成空串，此时 s 为了匹配它，方式只有1种：什么字符也不用挑（或 s 也是空串，什么都不做就匹配了，方式数也是1）
# 2) 小到 s 变成空串，但 t 不是，s 怎么也匹配不了 t，方式数为 0
for i in range(s_len+1):
    for j in range(t_len+1):
        if j==0: dp[i][j] = 1 # 小到 t 变成空串
        # elif i==0:dp[i][j] = 0
        else:
            if s[i-1] == t[j-1]:
                # 核心是选or不选
                # 最后一个字符可以匹配
                # 情况一：用s的第i个字母匹配t的第j个字符，有 dp[i-1][j-1] 个匹配情况；
                # 情况二：不用s的第i个字母去匹配t的第j个字母, 情况就等于 dp[i-1][j]；
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j] # 为什么还要加没有配上的case呢？
            else:
                # 从s中挑选，最后一个字符不匹配，那么这个字符有和没有情况是一样的
                dp[i][j] = dp[i-1][j]
```

### LC10.正则表达式匹配

[LC10.正则表达式匹配](https://leetcode-cn.com/problems/regular-expression-matching/solution/shou-hui-tu-jie-wo-tai-nan-liao-by-hyj8/) 题目：给你一个字符串 `s` 和一个字符规律 `p`，请你来实现一个支持 `'.'` 和 `'*'` 的正则表达式匹配。翻译一下，p能不能变成s。

状态定义：`dp[i][j]`表示`s`的前`i`个字符与`p`的前`j`个字符是否能够匹配，Ture or False问题。

1. p[-1] 有3种情况，`. * 字符`。
2. `p[-1]=='*'`又有3种情况，`*`让它前面的字符出现`0/1/n`次。

转移方程，

```python
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
dp = [[False] * (p_len+1) for _ in range(s_len+1)] # 状态定义

# 出口，用p的前0个字符去匹配s的前0个字符
# 1、s为空，p为空，能匹配上
dp[0][0] = True
# 2、p为空，s不为空，必为false(boolean数组默认值为false，无需处理)
# 3、s为空，p不为空，由于*可以匹配0个字符，所以有可能为true
"""
base case
p为空串，s不为空串，肯定不匹配。
- s为空串，但p不为空串，要想匹配，只可能是右端是星号，它干掉一个字符后，把 p 变为空串。
s、p都为空串，肯定匹配。
"""
for j in range(1, p_len+1):
    if p[j-1]=='*': dp[0][j] = dp[0][j-2]

# 4、填表（状态转移）
for i in range(1, s_len+1):
    for j in range(1, p_len+1):
        # dp[i][j]表示s的前i个字符s[0:i-1]与p的前j个字符p[0:j-1]是否匹配
        if s[i-1]==p[j-1] or p[j-1]=='.':
            dp[i][j] = dp[i-1][j-1]
        # *特判, *可以让它前面的字符出现0-n次
        if p[j-1]=='*':
            if s[i-1]==p[j-2] or p[j-2]=='.':
                # dp[i][j] = dp[i-1][j-2] # *让它前面的字符出现1次,  aa与a*以及 aa与.*
                # dp[i][j] = dp[i-1][j-3] # *让它前面的字符出现0次， aa与aac*
                # 还可以dp[i][j] = dp[i][j-2]
                # dp[i][j] = dp[i-1][j] # *让它前面的字符出现多次， aaaaaaa与a*
                dp[i][j] = dp[i][j-2] or dp[i-1][j-2] or dp[i-1][j]
            elif s[i-1]!=p[j-2]: # a与ab*, 干掉b
                dp[i][j] = dp[i][j-2]
```

### LC1143.最长公共子序列

[LC1143.最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/solution/fu-xue-ming-zhu-er-wei-dong-tai-gui-hua-r5ez6/)

状态定义：`dp[i][j]` 表示 `text1[0:i-1]` 和 `text2[0:j-1]` 的最长公共子序列。

> （注：`text1[0:i-1]` 表示的是 text1 的 第 0 个元素到第 i - 1 个元素，两端都包含）
> 之所以 `dp[i][j]` 的定义不是 text1[0:i] 和 text2[0:j] ，是为了方便当 i = 0 或者 j = 0 的时候，`dp[i][j]`表示为空字符串和另外一个字符串的匹配，这样 `dp[i][j]` 可以初始化为 0。

转移方程，

```python
for i in range(1, m+1):
    for j in range(1, n+1):
        # 举个例子，比如对于 ace 和 bc 而言，
        # 他们的最长公共子序列的长度等于 ① ace 和 b 的最长公共子序列长度0;
        # ② ac 和 bc 的最长公共子序列长度1 的最大值，即 1。
        if text1[i-1]==text2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

-----

### LC62.不同路径

[62. 不同路径](https://leetcode-cn.com/problems/unique-paths/)

状态定义：`到达网格(i,j)时, 共有 dp[i][j] 种走法。`

转移方程：

```python
# 左上角到右下角，每次只能向下或者向右移动一步。问总共有多少条不同的路径？
dp = [[0 for j in range(n)] for i in range(m)] # 不用表示空字符
dp[i][j] = dp[i-1][j]+dp[i][j-1] # 将向右和向下两条路径的方案数相加起来。
```

### LC63.不同路径2

[63. 不同路径 II](https://leetcode-cn.com/problems/unique-paths-ii/)与LC62不同，本次路径中障碍物，不能走。

状态定义：`dp[i][j]表示从(0,0)走到(i,j)的所有不同路径的方案数`。

转移方程：

```python
# 重点：如果网格 (i, j) 上有障碍物，则 dp[i][j] 值为 0，表示走到该格子的方案数为 0；
# dp[0][0] = 1，从(0,0)到达(0,0)只有一条路径
for i in range(1,m):
  for j in range(1,n):
    if obstacleGrid[i][j]==0: # 多一个限制条件，不是障碍物的时候才转移。
      dp[i][j] = dp[i-1][j]+dp[i][j-1]
```

### LC64.最小路径和

状态定义，

转移方程

### LC120.三角形最小路径和

[LC120.三角形最小路径和](https://leetcode-cn.com/problems/triangle/solution/di-gui-ji-yi-hua-dp-bi-xu-miao-dong-by-sweetiee/) 题目：给定一个三角形 `triangle` ，找出自顶向下的最小路径和。

**注意点：从下开始向上推。**

状态定义：`dp[i][j]`为从点`(i,j)`到<u>底边</u>的最小路径和。

转移方程，

```python
dp = [[0]*(m+1) for _ in range(m+1)] # (i,j)点到底边的最小路径和
# [i,j]
# [i+1,j] [i+1,j+1]
for i in range(m-1, -1, -1):
    for j in range(i, -1, -1):
        # 到达[i,j]的最短路径
        dp[i][j] = min(dp[i+1][j],dp[i+1][j+1])+triangle[i][j]
        ## 从三角形的最后一行开始递推，如下循环也ok
        # for (int i = n - 1; i >= 0; i--) 
        #     for (int j = 0; j <= i; j++) 
        return dp[0][0]
```

### LC174.地下城游戏（没做）

（不是特别重要，没考过）



### LC221.最大正方形

[LC221.最大正方形](https://leetcode-cn.com/problems/maximal-square/solution/li-jie-san-zhe-qu-zui-xiao-1-by-lzhlyle/) 题目：在一个由 `'0'` 和 `'1'` 组成的二维矩阵内，找到只包含 `'1'` 的最大正方形，并返回其面积。

状态定义：`dp[i][j]` 以 `matrix[i][j] `为右下角的正方形的最大边长。

转移方程，

```python
# dp[i][j] 以 matrix[i-1][j-1] 为右下角的正方形的最大边长
# dp = [[0]*(n+1) for _ in range(m+1)] 
for i in range(0, m):
    for j in range(0, n):
        # //base case
        # 初始化边界值
        if (i == 0 or j == 0):
            dp[i][j] = int(matrix[i][j])
            if matrix[i][j]=='1':
                # 状态方程为什么这样呢？具体看链接里的图
                dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
                max_side = max(max_side, dp[i][j]) # 记录最大边
# dp[i-1][j-1] 左上也记录的原因？
# 若形成正方形（非单 1），以当前为右下角的视角看，则需要：当前格、上、左、左上都是 1
```

### LC647.回文子串

[LC647.回文子串](https://programmercarl.com/0647.%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2.html#_647-%E5%9B%9E%E6%96%87%E5%AD%90%E4%B8%B2) 题目给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

状态定义：`dp[i][j]`表示区间范围`[i,j]` （注意是左闭右闭）的子串是否是回文子串。

输入："aaa" 输出：6 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"。

【注意】矩阵遍历一定要从下到上，从左到右遍历，这样保证`dp[i + 1][j - 1]`都是经过计算的。

转移方程：

```python
# 从下到上
for i in range(len(s)-1, -1, -1):
    # 从左到右
    # 因为dp[i][j]的定义，所以j一定是大于等于i的，那么在填充dp[i][j]的时候一定是只填充右上半部分
    for j in range(i, len(s)):
        if s[i] == s[j]:
            if j-i <= 1: # a, aa
                res += 1
                dp[i][j] = True
             elif dp[i+1][j-1]: # cabac
              	res += 1
              	dp[i][j] = True
return res
```

# 股票问题



# 丑数



