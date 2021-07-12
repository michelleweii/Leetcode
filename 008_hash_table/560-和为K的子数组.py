"""
先对原数组求个前缀和
求前缀和技巧：sum表示前缀和
i-j前缀的和为
nums[i...j]=sum[j]-sum[i-1]
"""
class Solution:
    def subarraySum(self, nums, k):
        hash_map = {}
        hash_map[0]=1 # 前缀和为0的数量有1个。默认nums[-1]=0
        res = 0
        sums = 0 # 前缀和
        for x in nums:
            sums += x
            res += hash_map.get(sums-k, 0) # hash_map[sums-k] KeyError: -1
            hash_map[sums] = hash_map.get(sums, 0) + 1

        return res


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2

    res = Solution()
    print(res.subarraySum(nums, k))

#
# nums = [1,2,5,9]
# n = len(nums)
# for i in range(n):
#     for j in range(i):
#         # print("idx----------------------",i,j)
#         # print("val",nums[i], nums[j])
#         print(i,j)
#
# print('-'*10)
#
# for k in range(n):
#     for m in range(k+1,n):
#         print(k,m)
#
