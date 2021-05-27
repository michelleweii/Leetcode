class Solution(object):
    def maxSlidingWindow(self, nums, k):
        # 单调队列
        res = []
        queue = []
        n = len(nums)
        if (n == 0 or k < 1 or n < k): return res
        if k==1: return nums
        for i in range(len(nums)):
            while queue and queue[0]<i-k+1:
                queue.pop(0)
            while queue and queue[0]<nums[i]:
                queue.pop()
            queue.append(nums[i])
            if i>=k-1:
                res.append(queue[0])
        return res

    # 暴力求解
    def maxSlidingWindow1(self, nums, k):
        if len(nums)==0:
            return [0]
        rs = []
        for i in range(len(nums)-k+1):
            tmp = max(nums[i:i+k])
            rs.append(tmp)
        return rs


if __name__ == '__main__':
    nums = [7,2,4]
        # [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2
    print(Solution().maxSlidingWindow(nums,k))

