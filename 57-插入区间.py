"""
middle
"""
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

"""
    def insert1(self, intervals, newInterval):
        i = 0
        n = len(intervals)
        while i < n and newInterval[0] > intervals[i][1]:
            i += 1
        left = i
        while i < n and newInterval[1] >= intervals[i][0]:
            i += 1
        right = i
        # print(left, right)
        if left >= n:
            res = intervals + [newInterval]
        elif left == right:
            # print(intervals)
            intervals.insert(left, newInterval)
            res = intervals
        else:
            res = intervals[:left] + [[min(intervals[left][0],\
                                           newInterval[0]), max(intervals[right - 1][1],
                                                                newInterval[1])]] + intervals[right:]
        return res
"""

