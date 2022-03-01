[其他「二分」相关题解](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/gong-shui-san-xie-xiang-jie-wei-he-yuan-xtam4/)

[为什么去除首尾相同元素就可以恢复二分的两端性](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/solution/gong-shui-san-xie-xiang-jie-wei-he-yuan-xtam4/)

<u>之前不明白为什么154相对于153的解决方案是“去除首尾元素”</u>

**<u>因为「二分」的本质是二段性，并非单调性。只要一段满足某个性质，另外一段不满足某个性质，就可以用「二分」。</u>**

LC153旋转数组最小值--> LC154(153升级版，有重复元素)--> LC33搜索旋转排序数组 (先找到最小值，确定target属于哪个递增区间，再次二分) --> LC81搜索旋转排序数组|| (LC33升级版，有重复元素【核心：恢复二段性】)