# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。
# 要求算法时间复杂度必须是O(n)。
import heapq
# 小顶堆
class Solution(object):
    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums)<3:
            return max(nums)

        nums = list(nums)
        print(nums)
        pq = []
        for x in nums:
            heapq.heappush(pq,x)
            if len(pq)>3: # 一直维护pq里只有3个元素
                heapq.heappop(pq) # 返回堆中最小的元素
        return pq[0]

def main():
    nums = [2,2,2,1,3,4,6,7]
    myResult = Solution()
    print(myResult.thirdMax(nums))

if __name__ == '__main__':
    main()

