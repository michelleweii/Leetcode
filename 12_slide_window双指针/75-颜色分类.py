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
        # https://leetcode-cn.com/problems/sort-colors/solution/kuai-su-pai-xu-partition-guo-cheng-she-ji-xun-huan/
        left = 0
        right = len(nums)
        cur = 0
        # 只移动0,2。 1自然会处于该处于的位置
        while cur < right:
            if nums[cur] == 0:
                nums[left], nums[cur] = nums[cur], nums[left]
                left += 1
                cur += 1
            elif nums[cur] == 2:
                right -= 1 # 这里先right--需要注意
                nums[right], nums[cur] = nums[cur], nums[right]
            else:
                cur += 1
        return nums



if __name__ == "__main__":
    nums = [2,0,1]#[2, 0, 2, 1, 1, 0]
    myresult = Solution()
    print(myresult.sortColors(nums))
