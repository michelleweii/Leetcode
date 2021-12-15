"""
hard 2021-10-26回顾 【单调递增栈】
思路：以第i根柱子为最矮柱子所能延伸的最大面积是什么？求每个矩形所在位置的最大值，分别向左延伸、向右延伸
res =（该矩形的高度）*（左右边界的距离）
注意！ 以第i个柱子为矮柱！
"""
class Solution:
    def largestRectangleArea(self, heights):
        heights = [0]+heights+[0]  # 插入两个哨兵
        # print(heights)
        stk = []
        res = 0
        for i in range(len(heights)):
            # 单调递增栈
            # 如果当前i元素小于栈顶元素，说明栈顶元素找到了它右边第一个比它小的元素
            # 在栈顶元素左侧，都是比栈顶元素小的。while一直向前计算，
            # 直到恢复单调递增栈
            while stk and heights[i]<heights[stk[-1]]: # <才是求比栈顶元素右边小的right
                h = heights[stk[-1]]
                stk.pop()
                res = max(res, (i-stk[-1]-1)*h)
            stk.append(i)
        return res

if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    # [2, 4]
    myresult = Solution()
    print(myresult.largestRectangleArea(heights))
