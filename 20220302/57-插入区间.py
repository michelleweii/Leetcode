"""
middle 2022-03-02
intervals = [[1,3],[6,9]], newInterval = [2,5]
[[1,5],[6,9]]
二分插入之后再套用56代码
https://leetcode-cn.com/problems/insert-interval/solution/python3er-fen-fa-by-simpleson/
https://mp.weixin.qq.com/s/ioUlNa4ZToCrun3qb4y4Ow
"""

# https://leetcode-cn.com/problems/insert-interval/solution/57-cha-ru-qu-jian-mo-ni-cha-ru-xiang-jie-by-carlsu/
class Solution:
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        # print(intervals)
        intervals.sort()
        # print(intervals)
        ans = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0]>ans[-1][1]:
                # 说明没有重叠，不合并
                ans.append(intervals[i])
            elif intervals[i][1]>ans[-1][1]:
                # 说明第一个if没有满足，相邻两个元素已经比较过了3>2，判断6>3即可
                ans[-1][1] = intervals[i][1]
        return ans

if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(Solution().insert(intervals,newInterval))