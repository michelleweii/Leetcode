"""
middle 双指针反向 O(N)
我的思考：
使用双指针的原因是根据这个问题的特点，存水的高度取决于两边较短的那个内壁的高度。
为什么这道题不用单调栈？
题解：https://leetcode-cn.com/problems/container-with-most-water/solution/container-with-most-water-shuang-zhi-zhen-fa-yi-do/
"""
class Solution:
    def maxArea(self, height):
        i, j = 0, len(height)-1
        res = 0
        while i<j:
            if height[i]<height[j]:
                res = max(res, height[i]*(j-i))
                i+=1
            else:
                res = max(res, height[j]*(j-i))
                j-=1
        return res


if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))