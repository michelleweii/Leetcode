"""
思路：
单调栈
求每个矩形所在位置的最大值，分别向左延伸、向右延伸
res =（该矩形的高度）*（左右边界的距离）
1、左边第一个比item小的位置
2、右边第一个比item小的位置
"""
class Solution:
    def largestRectangleArea(self, heights):
        stk_l, stk_r = [], []
        hash_l, hash_r = {}, {}
        for i in range(len(heights)-1):
            hash_r[i] = 0
            hash_l[i] = 0

        # 右边第一个比item小的位置
        for i in range(len(heights)-1):
            while(stk_r and heights[i]<heights[stk_r[-1]]):
                hash_r[stk_r.pop()] = i
            stk_r.append(i)
        print("hash_r:\n", hash_r)

        # 左边边第一个比item小的位置
        for i in range(len(heights)-1,-1,-1):
            while(stk_l and heights[i]<heights[stk_l[-1]]):
                hash_l[stk_l.pop()] = i
            stk_l.append(i)
        print("hash_l:\n", hash_l)

        res = 0
        for i in range(len(heights)-1):
            res = max(res, heights[i]*(hash_r[i]-hash_l[i]-1))
        return res




if __name__ == '__main__':
    heights = [2,4]#[2,1,5,6,2,3]
    myresult = Solution()
    print(myresult.largestRectangleArea(heights))
