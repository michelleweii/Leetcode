"""
middle
双指针[荷兰国旗问题] left,right指向边界，cur用来遍历
https://leetcode-cn.com/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/
"""
class Solution(object):
    def sortColors(self, nums):
        if len(nums)<2: return
        # 定义左右AB两条线，left & right

        # all in [0, left) = 0
        # all in [left, cur) = 1
        # all in [right, len - 1] = 2

        left, right = 0, len(nums)-1
        # cur是当前遍历的元素
        cur = 0
        while cur<=right:
            if nums[cur]==0:
                # left向右移动
                nums[cur], nums[left] = nums[left], nums[cur]
                cur += 1
                left += 1

            elif nums[cur] == 1:
                cur += 1

            # 与当前元素交换，b线向左移，elif nums[cur]==2:
            else:
                nums[cur], nums[right] = nums[right], nums[cur]
                right -= 1

        return nums



if __name__ == "__main__":
    nums = [2,0,1]#[2, 0, 2, 1, 1, 0]
    myresult = Solution()
    print(myresult.sortColors(nums))
