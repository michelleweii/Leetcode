"""
思路：
单调栈
求每个矩形所在位置的最大值，分别向左延伸、向右延伸
res =（该矩形的高度）*（左右边界的距离）
1、左边第一个比item小的位置
2、右边第一个比item小的位置

//单调递增栈,对于每一个柱子来说,朴素的思路就是记录左右两侧比它
//高度低的第一个柱子,得到当前柱子的高能够组成的最大矩形面积
//单调栈的性质自然地能够记录左边低柱子的下标,而右侧只需在每次
//遍历元素时决定是入栈或者计算面积即可.
"""
class Solution:
    def largestRectangleArea(self, heights):
        heights = [0]+heights+[0]  # 插入两个哨兵
        # print(heights)
        stk = []
        res = 0
        for i in range(len(heights)):
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
