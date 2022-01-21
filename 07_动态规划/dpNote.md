Fighting!

# 一维DP

明确概念，

- 数组：要求连续`i-1, i, i+1`;
- 子序列：不要求连续`i-3, i, i+5`;



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

删除一个元素`dp[i][j]=dp[i-1][j]+1，

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



### LC221.最大正方形



### LC1143.最长公共子序列



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

### LC120.三角形最小路径和



### LC174.地下城游戏



### LC647.回文子串



# 股票问题



# 丑数



