class Solution(object):
    def trap(self, height):
        # 根据短的那一端向高的那一端靠拢
        # 然后过程中更新左右最高的柱子，来求的中间的蓄水量
        # 这个蓄水量怎么求呢？area-中间一些柱子的高度
        low = 0
        high = len(height)-1
        while low<high:
            # 那么这个面积如何考虑呢？
            area = (high-low)*min(height[low],height[high])-面积
            if height[low]<height[high]:
                area = area if (high-low)*height[low]>area else (high-low)*height[low]>area
                low = low + 1
            else:
                # 水高由面积短的决定，此时是high短，所以由high决定
                area = area if (high-low)*height[high]>area else (high-low)*height[high]>area
                high = high-1
        return area


if __name__ == '__main__':

    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))
