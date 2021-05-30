"""
hard 有考过
单调栈
"""
class Solution:
    def trap(self, height):
        if len(height) <= 1:
            return 0
        res = 0
        stk = []
        """
        方法2
        for i in range(len(height)):
            while stk and height[stk[-1]]<=height[i]:
                j = stk[-1]
                stk.pop()
                if stk:
                    h = min(height[i],height[stk[-1]])
                    res += (h-height[j])* (i-stk[-1]-1)
            stk.append(i)
        return res
        """
        # 维护单调递增栈
        for i in range(len(height)):
            level = 0
            while stk and height[stk[-1]]<=height[i]:
                res += (height[stk[-1]]-level)*(i-stk[-1]-1)
                level = height[stk[-1]]
                stk.pop()
            if stk:
                res+=(height[i]-level)*(i-stk[-1]-1) # 这一句还是不明白？
            stk.append(i)
        return res

if __name__ == '__main__':
    height = [4,2,0,3,2,5]
    myresult = Solution()
    print(myresult.trap(height))