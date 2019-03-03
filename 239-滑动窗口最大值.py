class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """


    # 暴力求解
    def maxSlidingWindow1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums)==0:
            return [0]
        rs = []
        for i in range(len(nums)-k+1):
            tmp = max(nums[i:i+k])
            rs.append(tmp)
        return rs




if __name__ == '__main__':
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(Solution().maxSlidingWindow(nums,k))

