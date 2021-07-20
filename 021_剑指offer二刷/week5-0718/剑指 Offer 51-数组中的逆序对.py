"""
hard 归并排序进阶
2021-07-21
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/solution/jian-zhi-offer-51-shu-zu-zhong-de-ni-xu-pvn2h/
"""
class Solution:
    def reversePairs(self, nums):
        self.tmp = [0] * len(nums)
        return self.merge_sort(nums, 0, len(nums)-1)

    def merge_sort(self, nums, l, r):
        # 终止条件
        if l >= r: return 0
        # 递归划分
        m = (l + r) // 2
        res = self.merge_sort(nums, l, m) + self.merge_sort(nums, m + 1, r)
        # 合并阶段
        i, j = l, m + 1
        self.tmp[l:r + 1] = nums[l:r + 1]
        for k in range(l, r + 1):
            if i == m + 1:
                nums[k] = self.tmp[j]
                j += 1
            elif j == r + 1 or self.tmp[i] <= self.tmp[j]:
                nums[k] = self.tmp[i]
                i += 1
            else:
                nums[k] = self.tmp[j]
                j += 1
                res += m - i + 1  # 统计逆序对
        return res

if __name__ == '__main__':
    nums = [7,5,6,4]
    print(Solution().reversePairs(nums))