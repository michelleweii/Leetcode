"""
二分 easy
做几遍忘几遍！！！
2021-07-13
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/solution/mian-shi-ti-11-xuan-zhuan-shu-zu-de-zui-xiao-shu-3/
"""
class Solution:
    def minArray(self, numbers):
        # numbers是原本是递增的
        n = len(numbers)-1
        if numbers[0]<numbers[n]: return numbers[0]




if __name__ == '__main__':
    numbers = [2,2,2,0,1]
    print(Solution().minArray(numbers))