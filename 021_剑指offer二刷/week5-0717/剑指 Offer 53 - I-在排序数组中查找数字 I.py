"""
easy
hashmap 2021-07-16 once ok
二分
"""
class Solution:
    def search_hash(self, nums, target):
        if not nums:return 0
        hashmap = {}
        for x in nums:
            hashmap[x] = hashmap.get(x,0)+1
        return hashmap.get(target,0)

    def search(self, nums, target):
        


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 10
    # nums = [1]
    # target = 1
    print(Solution().search(nums, target))