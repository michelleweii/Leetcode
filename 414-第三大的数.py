# 给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。
# 要求算法时间复杂度必须是O(n)。
# gg
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # listnum = sorted(list(set(nums)))  # set之后是有序的
        #
        # if len(listnum)<3:
        #     # print(listnum)
        #     return max(listnum)
        #
        # listnum.reverse()
        # return listnum[2]





def main():
    nums = [2,2,2,1,3]
    myResult = Solution()
    print(myResult.thirdMax(nums))

if __name__ == '__main__':
    main()

