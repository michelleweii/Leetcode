class Solution(object):
    def maxArea(self, height):
        # 暴力 43/50
        # res = 0
        # for i in range(len(height)-1): # i是起始点
        #     for j in range(1,len(height)): # j是终止点
        #         w = j-i
        #         h = min(height[i],height[j])
        #         res = max(res,w*h)
        # return res

        # 贪心——谁短谁不要
        if not height or len(height) == 1:
            return 0
        low = 0
        high = len(height)-1
        area = (high-low)*min(height[low],height[high])
        while low<high:
            if height[low]<height[high]: # 谁短谁不要，low短
                area = area if area>height[low]*(high-low) else height[low]*(high-low)
                low += 1
            else:
                # high短
                area = area if area>height[high]*(high-low) else height[high]*(high-low)
                high -= 1
        return area


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))