class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 在连续递增，递减时，只保留首尾元素
        def wigglelength(type,nums):
            if (len(nums)==0): return 0
            # pre来保存已生成的摆动序列的最后一个值
            pre,cnt = nums[0],1
            for i in range(1,len(nums)):
                if type and pre<nums[i]:
                    cnt+=1
                    type = False
                elif not type and pre>nums[i]:
                    cnt+=1
                    type=True

                pre = nums[i] # 摆动序列的最后一个值

            return cnt

        # 后比前大，遍历一次; 前比后大，遍历一次
        return max(wigglelength(True,nums),wigglelength(False,nums))




if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9]
    print(Solution().wiggleMaxLength(nums))